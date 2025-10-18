"""Knowledge Base client for retrieving company information."""

import boto3
from typing import Dict, Any
from botocore.exceptions import ClientError

from ..core.config import CompanyConfiguration


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
            response = self._client.retrieve(
                knowledgeBaseId=company_config.knowledge_base_id,
                retrievalQuery={'text': query},
                retrievalConfiguration={
                    'vectorSearchConfiguration': {
                        'numberOfResults': 5
                    }
                }
            )

            return self._process_results(response, query)

        except ClientError as e:
            return {
                'success': False,
                'error': f"AWS Error: {e.response['Error']['Message']}",
                'raw_content': "Unable to retrieve information from knowledge base"
            }
        except Exception as e:
            return {
                'success': False,
                'error': f"Error: {str(e)}",
                'raw_content': "Unable to retrieve information from knowledge base"
            }
    
    def _process_results(
        self,
        response: Dict[str, Any],
        query: str
    ) -> Dict[str, Any]:
        """Process retrieval results and return raw content.
        
        Args:
            response: AWS Bedrock retrieval response
            query: Original user query
            
        Returns:
            Dictionary containing processed results and metadata
        """
        results = response.get('retrievalResults', [])

        if not results:
            return {
                'success': False,
                'error': 'No information found',
                'raw_content': 'No information found'
            }

        content_parts = []
        for result in results:
            content = result.get('content', {}).get('text', '')
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
            'result_count': len(content_parts)
        }
