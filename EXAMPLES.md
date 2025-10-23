# StatLock - Usage Examples

This document provides detailed examples of how to use StatLock for sports betting analysis.

## Example 1: Basic Chat Interaction

```python
from src.sports_betting_chatbot import SportsBettingChatbot

# Initialize the chatbot
chatbot = SportsBettingChatbot()

# Ask general questions
response = chatbot.chat("What are the key factors to consider when betting on NBA games?")
print(response)

# Get betting advice
response = chatbot.chat("Should I bet on favorites or underdogs?")
print(response)

# Learn about betting concepts
response = chatbot.explain_betting_concept("expected value in sports betting")
print(response)
```

## Example 2: Game Analysis

```python
from src.sports_betting_chatbot import SportsBettingChatbot
from src.models import Game, Team, BettingOdds
from datetime import datetime, timedelta

chatbot = SportsBettingChatbot()

# Create a game (NFL example)
game = Game(
    game_id="nfl_001",
    home_team=Team(name="Kansas City Chiefs", abbreviation="KC", wins=11, losses=2),
    away_team=Team(name="Buffalo Bills", abbreviation="BUF", wins=10, losses=3),
    game_time=datetime.now() + timedelta(days=1),
    sport="football"
)

# Add betting odds
odds = BettingOdds(
    game_id="nfl_001",
    spread=-2.5,  # Chiefs favored by 2.5
    over_under=52.5,
    moneyline_home=-140,
    moneyline_away=+120
)

# Get comprehensive analysis
analysis = chatbot.analyze_game(game, odds)
print("Game Analysis:")
print(analysis)
```

## Example 3: Getting Pick Recommendations

```python
from src.sports_betting_chatbot import SportsBettingChatbot
from src.models import Game, Team, BettingOdds
from datetime import datetime

chatbot = SportsBettingChatbot()

# NBA game example
game = Game(
    game_id="nba_001",
    home_team=Team(name="Golden State Warriors", abbreviation="GSW", wins=35, losses=32),
    away_team=Team(name="Los Angeles Lakers", abbreviation="LAL", wins=38, losses=29),
    game_time=datetime.now(),
    sport="basketball"
)

odds = BettingOdds(
    game_id="nba_001",
    spread=-4.5,
    over_under=225.5,
    moneyline_home=-180,
    moneyline_away=+155
)

# Get spread pick
spread_pick = chatbot.get_pick_recommendation(game, odds, "spread")
print("Spread Pick:")
print(spread_pick)
print("\n")

# Get over/under pick
ou_pick = chatbot.get_pick_recommendation(game, odds, "over_under")
print("Over/Under Pick:")
print(ou_pick)
print("\n")

# Get moneyline pick
ml_pick = chatbot.get_pick_recommendation(game, odds, "moneyline")
print("Moneyline Pick:")
print(ml_pick)
```

## Example 4: Bankroll Management

```python
from src.sports_betting_chatbot import SportsBettingChatbot

chatbot = SportsBettingChatbot()

# Get advice for different bankroll sizes and risk levels
advice_conservative = chatbot.bankroll_advice(bankroll=1000, risk_tolerance="conservative")
print("Conservative Approach ($1000 bankroll):")
print(advice_conservative)
print("\n")

advice_moderate = chatbot.bankroll_advice(bankroll=5000, risk_tolerance="moderate")
print("Moderate Approach ($5000 bankroll):")
print(advice_moderate)
print("\n")

advice_aggressive = chatbot.bankroll_advice(bankroll=10000, risk_tolerance="aggressive")
print("Aggressive Approach ($10000 bankroll):")
print(advice_aggressive)
```

## Example 5: Multiple Games Analysis

```python
from src.sports_betting_chatbot import SportsBettingChatbot
from src.models import Game, Team, BettingOdds
from datetime import datetime, timedelta

chatbot = SportsBettingChatbot()

# Analyze multiple games in a session
games = [
    {
        "game": Game(
            game_id="001",
            home_team=Team(name="Celtics", wins=50, losses=20),
            away_team=Team(name="Nets", wins=35, losses=35),
            game_time=datetime.now() + timedelta(hours=2),
            sport="basketball"
        ),
        "odds": BettingOdds(game_id="001", spread=-8.5, over_under=220.5)
    },
    {
        "game": Game(
            game_id="002",
            home_team=Team(name="Heat", wins=42, losses=28),
            away_team=Team(name="76ers", wins=45, losses=25),
            game_time=datetime.now() + timedelta(hours=3),
            sport="basketball"
        ),
        "odds": BettingOdds(game_id="002", spread=+2.5, over_under=215.5)
    }
]

print("Analyzing tonight's slate:\n")
for idx, game_data in enumerate(games, 1):
    print(f"--- Game {idx} ---")
    analysis = chatbot.analyze_game(game_data["game"], game_data["odds"])
    print(analysis)
    print("\n")
```

## Example 6: Learning Mode

```python
from src.sports_betting_chatbot import SportsBettingChatbot

chatbot = SportsBettingChatbot()

# Learn various betting concepts
concepts = [
    "What is value betting?",
    "Explain the Kelly Criterion",
    "What is line shopping?",
    "How do closing line value work?",
    "What are correlated parlays?"
]

print("Betting Education Session:\n")
for concept in concepts:
    print(f"Q: {concept}")
    response = chatbot.chat(concept)
    print(f"A: {response}\n")
    print("-" * 80)
    print()
```

## Example 7: Conversation Flow

```python
from src.sports_betting_chatbot import SportsBettingChatbot

chatbot = SportsBettingChatbot()

# Have a natural conversation
print("User: I have $2000 to start betting on NBA games. Where should I start?")
response1 = chatbot.chat("I have $2000 to start betting on NBA games. Where should I start?")
print(f"StatLock: {response1}\n")

print("User: What unit size should I use?")
response2 = chatbot.chat("What unit size should I use?")
print(f"StatLock: {response2}\n")

print("User: Should I bet on every game or be selective?")
response3 = chatbot.chat("Should I bet on every game or be selective?")
print(f"StatLock: {response3}\n")

# Clear conversation and start fresh
chatbot.clear_conversation()
print("\n[Conversation cleared]\n")

print("User: Tell me about parlay betting")
response4 = chatbot.chat("Tell me about parlay betting")
print(f"StatLock: {response4}")
```

## Example 8: Batch Processing

```python
from src.sports_betting_chatbot import SportsBettingChatbot
from src.models import Game, Team, BettingOdds
from datetime import datetime
import json

chatbot = SportsBettingChatbot()

# Process multiple picks and save results
picks_data = []

games = [
    # Add your games here
]

for game_data in games:
    pick = chatbot.get_pick_recommendation(
        game_data["game"], 
        game_data["odds"], 
        "spread"
    )
    
    picks_data.append({
        "game_id": game_data["game"].game_id,
        "matchup": f"{game_data['game'].away_team.name} @ {game_data['game'].home_team.name}",
        "pick": pick,
        "timestamp": datetime.now().isoformat()
    })

# Save to file for tracking
with open("daily_picks.json", "w") as f:
    json.dump(picks_data, f, indent=2)

print(f"Generated {len(picks_data)} picks and saved to daily_picks.json")
```

## Tips for Best Results

1. **Be Specific**: When asking for analysis, provide as much detail as possible about teams, records, and betting lines.

2. **Context Matters**: The chatbot maintains conversation history, so you can ask follow-up questions that build on previous responses.

3. **Clear History When Needed**: If you're switching topics, use `clear_conversation()` to reset the context.

4. **Combine Features**: Use game analysis first, then ask for specific pick recommendations based on the analysis.

5. **Learn First**: Use the education features to understand betting concepts before making picks.

6. **Risk Management**: Always ask for bankroll advice and follow proper betting unit sizing.

7. **Multiple Perspectives**: Ask the same question in different ways to get comprehensive insights.

## Running Examples

Save any example above to a file (e.g., `example.py`) and run:

```bash
python example.py
```

Make sure you have:
- Installed dependencies: `pip install -r requirements.txt`
- Set up your `.env` file with your OpenAI API key

## Interactive Testing

For quick testing, use the main application:

```bash
# Interactive mode
python main.py

# Demo mode
python main.py --demo
```
