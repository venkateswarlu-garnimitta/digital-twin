"""Knowledge Base client for retrieving company information."""

import boto3
from typing import Dict, Any
from botocore.exceptions import ClientError

from ..core.config import CompanyConfiguration


class KnowledgeBaseClient:
    """Client for retrieving information from AWS Bedrock Knowledge Base."""
    
    def __init__(self, region_name: str = "us-east-1"):
        """Initialize the Knowledge Base client."""
        self._client = boto3.client('bedrock-agent-runtime', region_name=region_name)
    
    def retrieve_company_information(
        self, 
        query: str, 
        company_config: CompanyConfiguration
    ) -> Dict[str, Any]:
        """
        Retrieve company-specific information from knowledge base.
        
        Args:
            query: User query
            company_config: Company configuration
            
        Returns:
            Dictionary containing raw retrieved information
        """
        try:
            # Execute retrieval request
            response = self._client.retrieve(
                knowledgeBaseId=company_config.knowledge_base_id,
                retrievalQuery={'text': query},
                retrievalConfiguration={
                    'vectorSearchConfiguration': {
                        'numberOfResults': 5
                    }
                }
            )
            
            # Process results
            return self._process_results(response, company_config.name, query)
            
        except ClientError as e:
            return {
                'success': False,
                'error': f"AWS Error: {e.response['Error']['Message']}",
                'raw_content': f"Unable to retrieve information about {company_config.name}"
            }
        except Exception as e:
            return {
                'success': False,
                'error': f"Error: {str(e)}",
                'raw_content': f"Unable to retrieve information about {company_config.name}"
            }
    
    def _process_results(
        self, 
        response: Dict[str, Any], 
        company_name: str, 
        query: str
    ) -> Dict[str, Any]:
        """Process retrieval results and return raw content."""
        results = response.get('retrievalResults', [])
        
        if not results:
            return {
                'success': False,
                'error': 'No information found',
                'raw_content': f'No information found about {company_name}'
            }
        
        # Extract raw content from results
        content_parts = []
        for result in results:
            content = result.get('content', {}).get('text', '')
            if content:
                content_parts.append(content.strip())
        
        if not content_parts:
            return {
                'success': False,
                'error': 'No relevant content found',
                'raw_content': f'No relevant content found about {company_name}'
            }
        
        # Return raw content for agent to process
        raw_content = "\n\n".join(content_parts)
        
        return {
            'success': True,
            'company': company_name,
            'raw_content': raw_content,
            'result_count': len(content_parts)
        }
