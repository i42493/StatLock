# Quick Start Guide

Get started with StatLock in 5 minutes!

## Step 1: Install Dependencies

### Option A: Automated Setup (Recommended)
```bash
chmod +x setup.sh
./setup.sh
```

### Option B: Manual Setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
```

## Step 2: Configure API Key

1. Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Open `.env` file
3. Replace `your_openai_api_key_here` with your actual API key:
   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   ```

## Step 3: Run the Chatbot

### Interactive Mode
```bash
python main.py
```

You'll see a prompt where you can chat with StatLock:
```
You: What are the best strategies for NBA betting?
StatLock: [AI provides detailed analysis]
```

### Demo Mode
```bash
python main.py --demo
```

This runs a demonstration with sample game data.

## Step 4: Try Some Examples

### Ask About Betting Strategies
```
You: How should I manage a $1000 bankroll?
You: What is value betting?
You: Should I use parlays?
```

### Get Game Analysis
See `EXAMPLES.md` for programmatic usage examples.

## Common Commands

- **Chat with the bot**: Just type your question
- **Clear conversation**: Type `clear`
- **Exit**: Type `quit` or `exit`

## Troubleshooting

### "No module named 'openai'"
Make sure you've installed dependencies:
```bash
pip install -r requirements.txt
```

### "OPENAI_API_KEY is required"
Edit your `.env` file and add your OpenAI API key.

### "Failed to create completion"
Check that:
1. Your API key is correct
2. You have credits in your OpenAI account
3. Your internet connection is working

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [EXAMPLES.md](EXAMPLES.md) for code examples
- Customize the chatbot behavior in `src/sports_betting_chatbot.py`

## Support

For issues or questions, please:
1. Check the documentation
2. Review the examples
3. Open an issue on GitHub

---

**Remember**: Always bet responsibly. This tool is for educational and entertainment purposes.
