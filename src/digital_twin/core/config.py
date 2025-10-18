"""Configuration management for Digital Twin application."""

import os
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class CompanyConfiguration:
    """Company configuration data structure.
    
    Attributes:
        name: Company display name
        industry: Industry category
        knowledge_base_id: AWS Bedrock knowledge base identifier
        source_id: Knowledge base source identifier
        description: Company description
    """
    name: str
    industry: str
    knowledge_base_id: str
    source_id: str
    description: str


class ConfigurationManager:
    """Configuration manager for the Digital Twin application."""

    def __init__(self) -> None:
        """Initialize configuration manager."""
        self.kb_id = os.getenv(
            "SHARED_KNOWLEDGE_BASE_ID", "shared-kb-id"
        )
        self.source_id = os.getenv(
            "KNOWLEDGE_BASE_SOURCE_ID", "shared-source-id"
        )

        self.companies = {
            "amazon": CompanyConfiguration(
                name="Amazon",
                industry="E-commerce",
                knowledge_base_id=self.kb_id,
                source_id=self.source_id,
                description="World's largest online retailer and cloud services provider"
            ),
            "walmart": CompanyConfiguration(
                name="Walmart",
                industry="E-commerce",
                knowledge_base_id=self.kb_id,
                source_id=self.source_id,
                description="Multinational retail corporation with extensive e-commerce operations"
            ),
            "fissionlabs": CompanyConfiguration(
                name="Fission Labs",
                industry="IT",
                knowledge_base_id=self.kb_id,
                source_id=self.source_id,
                description="Technology solutions provider specializing in AI, cloud, and data engineering"
            ),
            "aws": CompanyConfiguration(
                name="Amazon Web Services",
                industry="IT",
                knowledge_base_id=self.kb_id,
                source_id=self.source_id,
                description="Leading cloud computing platform and services provider"
            )
        }
    
    def get_industries(self) -> List[str]:
        """Get list of available industries.
        
        Returns:
            Sorted list of unique industry names
        """
        industries = set()
        for config in self.companies.values():
            industries.add(config.industry)
        return sorted(list(industries))

    def get_companies_by_industry(
        self, industry: str
    ) -> List[Dict[str, str]]:
        """Get companies for a specific industry.
        
        Args:
            industry: Industry name to filter by
            
        Returns:
            List of company dictionaries matching the industry
        """
        companies = []
        for key, config in self.companies.items():
            if config.industry == industry:
                companies.append({
                    "key": key,
                    "name": config.name,
                    "description": config.description,
                    "industry": config.industry
                })
        return companies

    def get_company_configuration(
        self,
        company_key: str
    ) -> Optional[CompanyConfiguration]:
        """Get configuration for a specific company.
        
        Args:
            company_key: Company identifier (case-insensitive)
            
        Returns:
            Company configuration if found, None otherwise
        """
        return self.companies.get(company_key.lower())

    def get_available_company_names(self) -> List[str]:
        """Get list of available company names.
        
        Returns:
            List of company display names
        """
        return [config.name for config in self.companies.values()]

    def get_available_company_keys(self) -> List[str]:
        """Get list of available company keys.
        
        Returns:
            List of company identifiers
        """
        return list(self.companies.keys())