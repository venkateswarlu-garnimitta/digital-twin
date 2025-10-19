"""Knowledge Base client for retrieving company information."""

import boto3
from typing import Dict, Any
from botocore.exceptions import ClientError

from ..core.config import CompanyConfiguration
from flotorch.sdk.memory import FlotorchVectorStore
import os
from dotenv import load_dotenv

load_dotenv()

vector_store = FlotorchVectorStore(
    base_url = os.getenv("FLOTORCH_BASE_URL"),
    api_key = os.getenv("FLOTORCH_API_KEY"),
    vectorstore_id= os.getenv("VECTOR_STORE_ID")
)

class KnowledgeBaseClient:
    """Client for retrieving information from AWS Bedrock Knowledge Base."""

    def __init__(self, region_name: str = "us-east-1") -> None:
        """Initialize the Knowledge Base client.
        
        Args:
            region_name: AWS region for the Bedrock client
        """
        self._client = boto3.client(
            'bedrock-agent-runtime', region_name=region_name
        )
    
    def retrieve_company_information(
        self,
        query: str,
        company_config: CompanyConfiguration
    ) -> Dict[str, Any]:
        """Retrieve information from knowledge base.
        
        Args:
            query: User query string (already enhanced with context)
            company_config: Company configuration object
            
        Returns:
            Dictionary containing raw retrieved information and metadata
        """
        try:
            result = vector_store.search(
                query=query,
                max_number_of_result=5
            )
            
            return self._process_flotorch_results(result, query)

        except Exception as e:
            return {
                'success': False,
                'error': f"Vector Store Error: {str(e)}",
                'raw_content': "Unable to retrieve information from knowledge base"
            }
    
    def _process_flotorch_results(
        self,
        response: Dict[str, Any],
        query: str
    ) -> Dict[str, Any]:
        """Process Flotorch Vector Store retrieval results and return raw content.
        
        Args:
            response: Flotorch Vector Store response
            query: Original user query
            
        Returns:
            Dictionary containing processed results and metadata
        """
        try:
            # Extract results from Flotorch Vector Store response
            results = response.get('data', [])
            
            if not results:
                return {
                    'success': False,
                    'error': 'No information found',
                    'raw_content': 'No information found'
                }

            content_parts = []
            for result in results:
                # Handle Flotorch Vector Store content format
                content_data = result.get('content', [])
                
                if isinstance(content_data, list):
                    # Extract text from content list
                    for content_item in content_data:
                        if isinstance(content_item, dict) and content_item.get('type') == 'text':
                            text_content = content_item.get('text', '')
                            if text_content:
                                content_parts.append(text_content.strip())
                elif isinstance(content_data, str):
                    # Direct string content
                    content_parts.append(content_data.strip())
                else:
                    # Try other possible field names
                    content = (result.get('text', '') or 
                              result.get('document', '') or
                              result.get('page_content', ''))
                    if content:
                        content_parts.append(content.strip())

            if not content_parts:
                return {
                    'success': False,
                    'error': 'No relevant content found',
                    'raw_content': 'No relevant content found'
                }

            raw_content = "\n\n".join(content_parts)

            return {
                'success': True,
                'raw_content': raw_content,
                'result_count': len(content_parts),
                'query': query
            }
            
        except Exception as e:
            print(f"DEBUG: Error processing Flotorch results: {str(e)}")
            return {
                'success': False,
                'error': f"Error processing results: {str(e)}",
                'raw_content': 'Error processing API response'
            }
    