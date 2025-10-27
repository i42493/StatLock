"""
StatLock - AI Sports Betting Chatbot
Main configuration module
"""

import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class for StatLock chatbot"""
    
    # OpenAI Configuration
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', '')
    CHATBOT_MODEL: str = os.getenv('CHATBOT_MODEL', 'gpt-4')
    CHATBOT_TEMPERATURE: float = float(os.getenv('CHATBOT_TEMPERATURE', '0.7'))
    CHATBOT_MAX_TOKENS: int = int(os.getenv('CHATBOT_MAX_TOKENS', '1000'))
    
    # Sports Data API Configuration
    SPORTS_API_KEY: str = os.getenv('SPORTS_API_KEY', '')
    SPORTS_API_URL: str = os.getenv('SPORTS_API_URL', 'https://api.sportsdata.io')
    
    @classmethod
    def validate(cls) -> bool:
        """Validate that required configuration is present"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required. Please set it in your .env file")
        return True


# Validate configuration on import
try:
    Config.validate()
except ValueError as e:
    print(f"Warning: {e}")
