"""
Sports Betting Chatbot
Main chatbot class that integrates ChatGPT for sports betting analysis
"""

from typing import Optional, List, Dict
from src.chatgpt_client import ChatGPTClient
from src.models import Pick, Game, Team, BettingOdds, PickAnalysis


class SportsBettingChatbot:
    """AI-powered sports betting assistant chatbot"""
    
    SYSTEM_PROMPT = """You are StatLock, an expert AI assistant for sports betting analysis. 
Your role is to help users make informed betting decisions by:
1. Analyzing games, teams, and matchups
2. Providing statistical insights and trends
3. Explaining betting concepts and strategies
4. Offering picks with detailed reasoning
5. Managing bankroll and risk management advice

You should:
- Be analytical and data-driven in your responses
- Explain your reasoning clearly
- Acknowledge uncertainty and risks
- Promote responsible gambling
- Never guarantee wins or make unrealistic promises
- Provide value through edge identification and probability analysis

Remember to always emphasize that sports betting involves risk and users should only bet what they can afford to lose.
"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the sports betting chatbot
        
        Args:
            api_key: OpenAI API key (optional, uses config if not provided)
        """
        self.chatgpt = ChatGPTClient(api_key=api_key)
        self.chatgpt.set_system_prompt(self.SYSTEM_PROMPT)
        
    def chat(self, user_message: str) -> str:
        """
        Send a message to the chatbot and get a response
        
        Args:
            user_message: The user's message/question
            
        Returns:
            The chatbot's response
        """
        return self.chatgpt.send_message(user_message)
    
    def analyze_game(self, game: Game, odds: Optional[BettingOdds] = None) -> str:
        """
        Get AI analysis for a specific game
        
        Args:
            game: Game object to analyze
            odds: Optional betting odds for the game
            
        Returns:
            AI analysis of the game
        """
        prompt = f"""Analyze this upcoming game:
{game.away_team.name} ({game.away_team.wins}-{game.away_team.losses}) @ {game.home_team.name} ({game.home_team.wins}-{game.home_team.losses})
Game Time: {game.game_time}
Sport: {game.sport}
"""
        
        if odds:
            prompt += f"\nBetting Lines:\n"
            if odds.spread:
                prompt += f"Spread: {odds.spread}\n"
            if odds.over_under:
                prompt += f"Over/Under: {odds.over_under}\n"
            if odds.moneyline_home and odds.moneyline_away:
                prompt += f"Moneyline: {game.home_team.name} {odds.moneyline_home} / {game.away_team.name} {odds.moneyline_away}\n"
        
        prompt += "\nProvide a detailed analysis including key factors, trends, and potential betting value."
        
        return self.chatgpt.send_message(prompt)
    
    def get_pick_recommendation(self, game: Game, odds: BettingOdds, bet_type: str) -> str:
        """
        Get a betting pick recommendation for a game
        
        Args:
            game: Game to get pick for
            odds: Betting odds
            bet_type: Type of bet (spread, over_under, moneyline)
            
        Returns:
            Pick recommendation with reasoning
        """
        prompt = f"""I need a {bet_type} pick for this game:
{game.away_team.name} ({game.away_team.wins}-{game.away_team.losses}) @ {game.home_team.name} ({game.home_team.wins}-{game.home_team.losses})

Current lines:
- Spread: {odds.spread}
- Over/Under: {odds.over_under}
- Moneyline: {odds.moneyline_home} / {odds.moneyline_away}

Provide your pick recommendation with:
1. Your predicted outcome
2. Confidence level (0-100%)
3. Key reasoning
4. Potential risks
5. Suggested stake size (conservative/moderate/aggressive)
"""
        
        return self.chatgpt.send_message(prompt)
    
    def explain_betting_concept(self, concept: str) -> str:
        """
        Get explanation of a betting concept or term
        
        Args:
            concept: The betting concept to explain
            
        Returns:
            Explanation of the concept
        """
        prompt = f"Please explain this sports betting concept or term: {concept}"
        return self.chatgpt.send_message(prompt)
    
    def bankroll_advice(self, bankroll: float, risk_tolerance: str = "moderate") -> str:
        """
        Get bankroll management advice
        
        Args:
            bankroll: Total bankroll amount
            risk_tolerance: Risk level (conservative, moderate, aggressive)
            
        Returns:
            Bankroll management advice
        """
        prompt = f"""I have a betting bankroll of ${bankroll} and my risk tolerance is {risk_tolerance}.
Please provide advice on:
1. Recommended unit size
2. Maximum bet sizes
3. Bankroll management strategy
4. Risk management tips
"""
        return self.chatgpt.send_message(prompt)
    
    def clear_conversation(self):
        """Clear the conversation history"""
        self.chatgpt.clear_history()
    
    def get_history(self) -> List[Dict[str, str]]:
        """Get conversation history"""
        return self.chatgpt.get_conversation_history()
