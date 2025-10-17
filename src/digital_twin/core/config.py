"""Configuration management for Digital Twin application."""

import os
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class CompanyConfiguration:
    """Company configuration."""
    name: str
    knowledge_base_id: str
    source_id: str
    description: str


class ConfigurationManager:
    """Configuration manager for the Digital Twin application."""
    
    def __init__(self):
        """Initialize configuration manager."""
        # Get configuration from environment
        self.kb_id = os.getenv("SHARED_KNOWLEDGE_BASE_ID", "shared-kb-id")
        self.source_id = os.getenv("KNOWLEDGE_BASE_SOURCE_ID", "shared-source-id")
        
        # Hardcoded companies
        self.companies = {
            "techcorp": CompanyConfiguration(
                name="TechCorp",
                knowledge_base_id=self.kb_id,
                source_id=self.source_id,
                description="Technology company"
            ),
            "financeinc": CompanyConfiguration(
                name="FinanceInc",
                knowledge_base_id=self.kb_id,
                source_id=self.source_id,
                description="Financial services company"
            ),
            "healthplus": CompanyConfiguration(
                name="HealthPlus",
                knowledge_base_id=self.kb_id,
                source_id=self.source_id,
                description="Healthcare company"
            ),
            "retailmax": CompanyConfiguration(
                name="RetailMax",
                knowledge_base_id=self.kb_id,
                source_id=self.source_id,
                description="Retail company"
            )
        }
    
    def get_company_configuration(self, company_key: str) -> Optional[CompanyConfiguration]:
        """Get configuration for a specific company."""
        return self.companies.get(company_key.lower())
    
    def get_available_company_names(self) -> List[str]:
        """Get list of available company names."""
        return [config.name for config in self.companies.values()]
    
    def get_available_company_keys(self) -> List[str]:
        """Get list of available company keys."""
        return list(self.companies.keys())
