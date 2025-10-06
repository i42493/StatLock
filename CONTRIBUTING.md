# Contributing to StatLock

Thank you for your interest in contributing to StatLock! This document provides guidelines for contributing to the project.

## Ways to Contribute

- 🐛 Report bugs
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Submit bug fixes
- ✨ Add new features
- 🧪 Write tests
- 📊 Add sports data integrations

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/StatLock.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes
6. Commit your changes: `git commit -m "Add your feature"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Create a Pull Request

## Development Setup

```bash
# Clone the repository
git clone https://github.com/i42493/StatLock.git
cd StatLock

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Add your OpenAI API key to .env
```

## Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and single-purpose
- Comment complex logic

## Testing Your Changes

Before submitting a pull request:

1. Test your code with the demo mode:
   ```bash
   python main.py --demo
   ```

2. Test interactive mode:
   ```bash
   python main.py
   ```

3. Verify your changes don't break existing functionality

## Pull Request Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Include examples of how to use new features
- Update documentation if needed
- Keep pull requests focused on a single feature or fix

## Code Structure

```
StatLock/
├── src/
│   ├── config.py               # Configuration management
│   ├── chatgpt_client.py       # ChatGPT API integration
│   ├── models.py               # Data models
│   └── sports_betting_chatbot.py # Main chatbot logic
├── main.py                     # Entry point
├── requirements.txt            # Dependencies
└── README.md                   # Documentation
```

## Feature Ideas

Some ideas for contributions:

### Integrations
- [ ] Add live sports data API integration (e.g., The Odds API, SportsData.io)
- [ ] Integration with sportsbooks APIs
- [ ] Discord/Telegram bot integration
- [ ] Web interface with Flask/FastAPI

### Features
- [ ] Historical performance tracking
- [ ] Pick history database
- [ ] Win/loss statistics
- [ ] ROI calculator
- [ ] Multiple AI models support (Claude, Gemini, etc.)
- [ ] Voice interface
- [ ] Mobile app

### Data & Analysis
- [ ] Advanced statistical models
- [ ] Machine learning predictions
- [ ] Injury data integration
- [ ] Weather data for outdoor sports
- [ ] Line movement tracking
- [ ] Sharp money indicators

### Monetization Features
- [ ] Subscription management system
- [ ] Payment processing integration
- [ ] Pick package generator
- [ ] Customer dashboard
- [ ] Email newsletter integration
- [ ] Affiliate tracking

## Reporting Bugs

When reporting bugs, please include:

- Description of the bug
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details (OS, Python version, etc.)
- Error messages or screenshots

## Suggesting Features

When suggesting features, please:

- Describe the feature clearly
- Explain the use case
- Provide examples if possible
- Consider how it fits with existing features

## Questions?

If you have questions about contributing, feel free to:
- Open an issue
- Start a discussion
- Contact the maintainers

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help create a positive community

## License

By contributing to StatLock, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to StatLock! 🎉
