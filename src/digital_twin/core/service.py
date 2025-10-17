"""Main service for Digital Twin application."""

from typing import Dict, Any, Optional, List

from .config import ConfigurationManager
from ..agents.manager import StrandsAgentManager


class DigitalTwinService:
    """Main service for the Digital Twin application."""
    
    def __init__(self, aws_region: str = "us-east-1"):
        """Initialize the service."""
        self._config_manager = ConfigurationManager()
        self._agent_manager = StrandsAgentManager(aws_region=aws_region)
    
    def process_query(
        self,
        company_key: str,
        user_query: str,
        session_id: str = None
    ) -> Dict[str, Any]:
        """Process a user query for a company."""
        try:
            # Validate inputs
            if not self._validate_inputs(company_key, user_query):
                return {
                    "success": False,
                    "error": "Invalid inputs"
                }
            
            # Get company configuration
            company_config = self._config_manager.get_company_configuration(company_key)
            if not company_config:
                return {
                    "success": False,
                    "error": f"Company '{company_key}' not found"
                }
            
            # Process query through Strands Agent
            if session_id:
                response = self._agent_manager.process_query(session_id, user_query)
            else:
                # Create new session
                session_result = self._agent_manager.create_new_session(
                    company_key, company_config, user_query
                )
                if not session_result['success']:
                    return session_result
                
                session_id = session_result['session_id']
                response = self._agent_manager.process_query(session_id, user_query)
            
            # Add session ID to response
            if response['success']:
                response['session_id'] = session_id
            
            return response
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Error: {str(e)}"
            }
    
    def get_available_companies(self) -> List[Dict[str, str]]:
        """Get list of available companies."""
        companies = []
        for key, config in self._config_manager.companies.items():
            companies.append({
                "key": key,
                "name": config.name,
                "description": config.description
            })
        return companies
    
    def get_service_status(self) -> Dict[str, Any]:
        """Get service status."""
        return {
            "service_status": "operational",
            "total_companies": len(self._config_manager.companies),
            "available_companies": self.get_available_companies()
        }
    
    def create_new_session(self, company_key: str, initial_query: str = None) -> Dict[str, Any]:
        """Create a new session."""
        try:
            company_config = self._config_manager.get_company_configuration(company_key)
            if not company_config:
                return {
                    "success": False,
                    "error": f"Company '{company_key}' not found"
                }
            
            return self._agent_manager.create_new_session(
                company_key, company_config, initial_query
            )
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to create session: {str(e)}"
            }
    
    def get_session_history(self, session_id: str) -> Dict[str, Any]:
        """Get session information."""
        return self._agent_manager.get_session_information(session_id)
    
    def list_user_sessions(self, limit: int = 20) -> Dict[str, Any]:
        """List active sessions."""
        try:
            sessions = self._agent_manager.list_active_sessions()
            return {
                "success": True,
                "sessions": sessions[:limit],
                "total_count": len(sessions)
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to list sessions: {str(e)}"
            }
    
    def switch_to_session(self, session_id: str) -> Dict[str, Any]:
        """Switch to a session."""
        return self._agent_manager.switch_to_session(session_id)
    
    def delete_session(self, session_id: str) -> Dict[str, Any]:
        """Delete a session."""
        return self._agent_manager.delete_session(session_id)
    
    def _validate_inputs(self, company_key: str, user_query: str) -> bool:
        """Validate inputs."""
        # Validate company key
        available_keys = self._config_manager.get_available_company_keys()
        if company_key.lower() not in [key.lower() for key in available_keys]:
            return False
        
        # Validate query
        if not user_query or not user_query.strip() or len(user_query.strip()) < 3:
            return False
        
        return True