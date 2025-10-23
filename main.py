"""
StatLock - AI Sports Betting Chatbot
Main application entry point
"""

import sys
from datetime import datetime
from src.sports_betting_chatbot import SportsBettingChatbot
from src.models import Game, Team, BettingOdds


def print_welcome():
    """Print welcome message"""
    print("=" * 60)
    print("  StatLock - AI Sports Betting Assistant")
    print("  Powered by ChatGPT")
    print("=" * 60)
    print("\nWelcome! I'm your AI assistant for sports betting analysis.")
    print("Ask me about games, betting strategies, or get pick recommendations.\n")
    print("Commands:")
    print("  - Type your question or request")
    print("  - 'clear' - Clear conversation history")
    print("  - 'quit' or 'exit' - Exit the application")
    print("=" * 60)
    print()


def demo_mode():
    """Run a demo with sample data"""
    print("\n--- DEMO MODE ---")
    print("Running with sample game data...\n")
    
    chatbot = SportsBettingChatbot()
    
    # Create sample game
    game = Game(
        game_id="demo_001",
        home_team=Team(name="Lakers", abbreviation="LAL", wins=45, losses=37),
        away_team=Team(name="Celtics", abbreviation="BOS", wins=57, losses=25),
        game_time=datetime.now(),
        sport="basketball"
    )
    
    odds = BettingOdds(
        game_id="demo_001",
        spread=-3.5,
        over_under=215.5,
        moneyline_home=-150,
        moneyline_away=+130
    )
    
    print(f"Analyzing: {game.away_team.name} @ {game.home_team.name}\n")
    
    try:
        analysis = chatbot.analyze_game(game, odds)
        print("AI Analysis:")
        print("-" * 60)
        print(analysis)
        print("-" * 60)
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure your OPENAI_API_KEY is set in the .env file")


def interactive_mode():
    """Run interactive chat mode"""
    chatbot = SportsBettingChatbot()
    print_welcome()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit']:
                print("\nThank you for using StatLock! Bet responsibly!")
                break
            
            if user_input.lower() == 'clear':
                chatbot.clear_conversation()
                print("\n[Conversation history cleared]\n")
                continue
            
            print("\nStatLock: ", end="")
            response = chatbot.chat(user_input)
            print(response)
            print()
            
        except KeyboardInterrupt:
            print("\n\nThank you for using StatLock! Bet responsibly!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Please check your configuration and try again.\n")


def main():
    """Main application entry point"""
    if len(sys.argv) > 1 and sys.argv[1] == '--demo':
        demo_mode()
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
