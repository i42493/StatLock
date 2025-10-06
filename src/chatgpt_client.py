"""
ChatGPT Integration Module
Handles communication with OpenAI's ChatGPT API
"""

from typing import List, Dict, Optional
from openai import OpenAI
from src.config import Config


class ChatGPTClient:
    """Client for interacting with ChatGPT API"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize ChatGPT client
        
        Args:
            api_key: OpenAI API key (uses Config.OPENAI_API_KEY if not provided)
        """
        self.api_key = api_key or Config.OPENAI_API_KEY
        self.client = OpenAI(api_key=self.api_key)
        self.model = Config.CHATBOT_MODEL
        self.temperature = Config.CHATBOT_TEMPERATURE
        self.max_tokens = Config.CHATBOT_MAX_TOKENS
        self.conversation_history: List[Dict[str, str]] = []
        
    def set_system_prompt(self, system_prompt: str):
        """
        Set the system prompt for the chatbot
        
        Args:
            system_prompt: The system prompt to use
        """
        self.conversation_history = [
            {"role": "system", "content": system_prompt}
        ]
    
    def send_message(self, message: str, include_history: bool = True) -> str:
        """
        Send a message to ChatGPT and get a response
        
        Args:
            message: The user message to send
            include_history: Whether to include conversation history
            
        Returns:
            The assistant's response
        """
        # Add user message to history
        user_message = {"role": "user", "content": message}
        
        if include_history:
            self.conversation_history.append(user_message)
            messages = self.conversation_history
        else:
            messages = [user_message]
        
        # Call OpenAI API
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        
        # Extract assistant's response
        assistant_message = response.choices[0].message.content
        
        # Add to conversation history
        if include_history:
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
        
        return assistant_message
    
    def clear_history(self):
        """Clear conversation history (except system prompt)"""
        if self.conversation_history and self.conversation_history[0]["role"] == "system":
            self.conversation_history = [self.conversation_history[0]]
        else:
            self.conversation_history = []
    
    def get_conversation_history(self) -> List[Dict[str, str]]:
        """Get the current conversation history"""
        return self.conversation_history.copy()
