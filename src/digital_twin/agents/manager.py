"""Strands Agent manager for Digital Twin application."""

import os
import uuid
import time
from typing import Dict, List, Any
from datetime import datetime

from strands.agent.agent import Agent
from strands.tools import tool
from strands.session.repository_session_manager import RepositorySessionManager
from flotorch.strands.llm import FlotorchStrandsModel
from flotorch.strands.session import FlotorchStrandsSession

from ..core.config import CompanyConfiguration
from ..knowledge.knowledge_base import KnowledgeBaseClient


class StrandsAgentManager:
    """Manager for Strands agents."""
    
    def __init__(self, aws_region: str = "us-east-1"):
        """Initialize the Strands Agent Manager."""
        self._knowledge_client = KnowledgeBaseClient(region_name=aws_region)
        self._active_agents: Dict[str, Dict[str, Any]] = {}
        
        # Flotorch configuration
        self._api_key = os.getenv("FLOTORCH_API_KEY", "")
        self._base_url = os.getenv("FLOTORCH_BASE_URL", "")
        self._model_id = os.getenv("FLOTORCH_MODEL_ID", "anthropic.claude-3-sonnet-20240229-v1:0")
    
    def create_new_session(
        self, 
        company_key: str, 
        company_config: CompanyConfiguration, 
        initial_query: str = None
    ) -> Dict[str, Any]:
        """Create a new Strands session for a company."""
        try:
            # Create knowledge tool
            knowledge_tool = self._create_knowledge_tool(company_config)
            
            # Create model and session
            model = FlotorchStrandsModel(
                model_id=self._model_id,
                api_key=self._api_key,
                base_url=self._base_url,
            )
            
            repository = FlotorchStrandsSession(
                api_key=self._api_key,
                base_url=self._base_url
            )
            
            session_id = str(uuid.uuid4())
            session_manager = RepositorySessionManager(
                session_id=session_id,
                session_repository=repository
            )
            
            # Create system prompt for concise responses
            system_prompt = """You are a helpful company representative.

IMPORTANT INSTRUCTIONS:
- Always provide SHORT, CONCISE answers like ChatGPT
- Keep responses under 200 words
- Use the knowledge base tool to get accurate information
- Give direct answers without unnecessary details
- Be conversational and helpful
- If you don't know something, say so clearly

Answer questions using the knowledge base tool when needed."""
            
            # Create agent
            agent = Agent(
                model=model,
                tools=[knowledge_tool],
                session_manager=session_manager,
                system_prompt=system_prompt
            )
            
            # Store agent info
            session_title = (
                initial_query[:50] + "..." 
                if initial_query and len(initial_query) > 50 
                else f"Chat with {company_config.name}"
            )
            
            self._active_agents[session_id] = {
                'agent': agent,
                'company_key': company_key,
                'company_name': company_config.name,
                'created_at': time.time(),
                'session_title': session_title
            }
            
            return {
                "success": True,
                "session_id": session_id,
                "company_name": company_config.name,
                "company_key": company_key,
                "session_title": session_title
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to create session: {str(e)}"
            }
    
    def process_query(self, session_id: str, query: str) -> Dict[str, Any]:
        """Process a query using an existing session."""
        try:
            if session_id not in self._active_agents:
                return {
                    "success": False,
                    "error": "Session not found"
                }
            
            agent_info = self._active_agents[session_id]
            agent = agent_info['agent']
            
            # Process query
            response = agent(query)
            
            return {
                "success": True,
                "response": str(response),
                "session_id": session_id,
                "company_name": agent_info['company_name']
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Error processing query: {str(e)}"
            }
    
    def get_session_information(self, session_id: str) -> Dict[str, Any]:
        """Get session information."""
        if session_id not in self._active_agents:
            return {
                "success": False,
                "error": "Session not found"
            }
        
        agent_info = self._active_agents[session_id]
        return {
            "success": True,
            "session_id": session_id,
            "company_name": agent_info['company_name'],
            "company_key": agent_info['company_key'],
            "session_title": agent_info['session_title']
        }
    
    def list_active_sessions(self) -> List[Dict[str, Any]]:
        """List all active sessions."""
        sessions = []
        for session_id, agent_info in self._active_agents.items():
            sessions.append({
                'session_id': session_id,
                'company_name': agent_info['company_name'],
                'company_key': agent_info['company_key'],
                'session_title': agent_info['session_title'],
                'created_at': agent_info['created_at'],
                'created_at_formatted': datetime.fromtimestamp(agent_info['created_at']).strftime('%Y-%m-%d %H:%M')
            })
        
        sessions.sort(key=lambda x: x['created_at'], reverse=True)
        return sessions
    
    def switch_to_session(self, session_id: str) -> Dict[str, Any]:
        """Switch to an existing session."""
        if session_id not in self._active_agents:
            return {
                "success": False,
                "error": "Session not found"
            }
        
        agent_info = self._active_agents[session_id]
        return {
            "success": True,
            "session_id": session_id,
            "company_name": agent_info['company_name'],
            "company_key": agent_info['company_key'],
            "session_title": agent_info['session_title']
        }
    
    def delete_session(self, session_id: str) -> Dict[str, Any]:
        """Delete a session."""
        if session_id in self._active_agents:
            del self._active_agents[session_id]
            return {
                "success": True,
                "message": "Session deleted successfully"
            }
        else:
            return {
                "success": False,
                "error": "Session not found"
            }
    
    def _create_knowledge_tool(self, company_config: CompanyConfiguration):
        """Create knowledge base tool for a company."""
        @tool
        def company_knowledge_tool(query: str) -> str:
            """Retrieve information about the company from knowledge base. Use this tool to get accurate, up-to-date information about the company."""
            try:
                result = self._knowledge_client.retrieve_company_information(
                    query, company_config
                )
                
                if result.get('success'):
                    # Return raw content for agent to process and summarize
                    return result.get('raw_content', 'No information found.')
                else:
                    return "Unable to retrieve information from knowledge base."
                    
            except Exception as e:
                return f"Error retrieving information: {str(e)}"
        
        return company_knowledge_tool