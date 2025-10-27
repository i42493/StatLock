"""
Sports Betting Models
Data models for sports betting analysis
"""

from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel, Field


class Team(BaseModel):
    """Represents a sports team"""
    name: str
    abbreviation: Optional[str] = None
    wins: int = 0
    losses: int = 0
    
    
class Game(BaseModel):
    """Represents a sports game"""
    game_id: str
    home_team: Team
    away_team: Team
    game_time: datetime
    sport: str = "unknown"
    home_score: Optional[int] = None
    away_score: Optional[int] = None
    status: str = "scheduled"  # scheduled, in_progress, completed
    

class BettingOdds(BaseModel):
    """Represents betting odds for a game"""
    game_id: str
    spread: Optional[float] = None
    over_under: Optional[float] = None
    moneyline_home: Optional[int] = None
    moneyline_away: Optional[int] = None
    

class Pick(BaseModel):
    """Represents a betting pick/prediction"""
    game: Game
    pick_type: str  # spread, over_under, moneyline
    prediction: str
    confidence: float = Field(ge=0.0, le=1.0)  # 0-1 scale
    reasoning: str
    timestamp: datetime = Field(default_factory=datetime.now)
    

class PickAnalysis(BaseModel):
    """Detailed analysis of a betting pick"""
    pick: Pick
    key_factors: List[str] = []
    risks: List[str] = []
    edge_percentage: Optional[float] = None
    recommended_stake: Optional[str] = None
