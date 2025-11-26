# The Price is Right - Deal Hunting Agentic AI

An autonomous multi-agent AI system that finds online deals by collaborating with a fine-tuned LLM, RAG pipeline, and traditional ML models.

## Overview

This project implements a sophisticated ensemble of AI agents that:
- Scrapes RSS feeds from deal websites
- Estimates true product values using multiple ML approaches
- Identifies significant discounts (deals)
- Sends real-time alerts for the best opportunities

## Architecture

### Multi-Agent System

1. **Planning Agent** - Orchestrates the entire workflow
2. **Scanner Agent** - Scrapes deals from RSS feeds using OpenAI Structured Outputs
3. **Ensemble Agent** - Combines predictions from three models:
   - **Specialist Agent**: Fine-tuned Llama 3.1-8B deployed on Modal
   - **Frontier Agent**: RAG pipeline using GPT-4o-mini/DeepSeek + ChromaDB
   - **Random Forest Agent**: Traditional ML with sentence embeddings
4. **Messaging Agent** - Sends alerts via Pushover or Twilio

## Features

- Real-time deal monitoring from multiple RSS feeds
- Ensemble ML approach combining fine-tuned LLM, RAG, and traditional ML
- ChromaDB vector database for similarity search
- Modal serverless GPU deployment for fine-tuned models
- Gradio web interface with auto-refresh
- Push notifications and SMS alerts
- Persistent memory to avoid duplicate alerts

## Installation

### Prerequisites

- Python 3.8+
- Modal account (for deployment)
- OpenAI API key
- Optional: Pushover or Twilio account for notifications

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/deal-hunter-ai.git
cd deal-hunter-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables in `.env`:
```bash
# Required
OPENAI_API_KEY=your_openai_key
MODAL_TOKEN_ID=your_modal_token_id
MODAL_TOKEN_SECRET=your_modal_token_secret

# Optional
DEEPSEEK_API_KEY=your_deepseek_key
PUSHOVER_USER=your_pushover_user
PUSHOVER_TOKEN=your_pushover_token
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_FROM=your_twilio_phone
MY_PHONE_NUMBER=your_phone_number
```

4. Set up Modal:
```bash
modal setup
```

5. Configure Modal secrets:
- Go to modal.com dashboard
- Create a secret named `hf-secret` with your HuggingFace token

## Usage

### Deploy the Pricer Service to Modal

```bash
modal deploy pricer_service2.py
```

### Run the Deal Agent Framework

```bash
python deal_agent_framework.py
```

### Launch the Gradio UI

```bash
python price_is_right.py
```

The UI will automatically:
- Load existing deals from memory
- Refresh every 60 seconds to find new deals
- Display product descriptions, prices, estimates, and discounts

### Run from Jupyter Notebooks

Explore the day-by-day progression:
- `day1.ipynb` - Modal setup and deployment basics
- `day2.0.ipynb` to `day2.4.ipynb` - Progressive feature building
- `day3.ipynb`, `day4.ipynb`, `day5.ipynb` - Advanced topics

## Project Structure

```
week8/
├── agents/
│   ├── agent.py              # Base agent class
│   ├── planning_agent.py     # Main orchestrator
│   ├── scanner_agent.py      # RSS scraper
│   ├── ensemble_agent.py     # Model ensemble coordinator
│   ├── specialist_agent.py   # Fine-tuned LLM agent
│   ├── frontier_agent.py     # RAG agent
│   ├── random_forest_agent.py # Traditional ML agent
│   ├── messaging_agent.py    # Alert system
│   └── deals.py              # Data models
├── deal_agent_framework.py   # Main framework
├── price_is_right.py         # Gradio UI
├── pricer_service.py         # Modal function deployment
├── pricer_service2.py        # Modal class deployment (cached)
├── pricer_ephemeral.py       # Ephemeral Modal deployment
├── items.py                  # Data processing utilities
├── testing.py                # Testing framework
├── memory.json               # Persistent deal memory
├── ensemble_model.pkl        # Trained ensemble model
├── random_forest_model.pkl   # Trained RF model
└── community_contributions/  # Student variations

```

## How It Works

1. **Scanning Phase**: Scanner Agent fetches deals from RSS feeds
2. **Selection Phase**: OpenAI filters top 5 deals with best descriptions/prices
3. **Estimation Phase**: Ensemble Agent gets predictions from all 3 models
4. **Aggregation Phase**: Linear regression combines predictions
5. **Alert Phase**: Deals with >$50 discount trigger notifications
6. **Memory Phase**: Persists deals to avoid duplicates

## Technologies Used

- **Modal**: Serverless GPU deployment
- **OpenAI GPT-4o-mini**: Deal scanning and structured outputs
- **Llama 3.1-8B**: Fine-tuned price estimation
- **ChromaDB**: Vector database for RAG
- **Scikit-learn**: Random Forest and Linear Regression
- **Gradio**: Web UI
- **Beautiful Soup**: Web scraping
- **Transformers**: LLM inference
- **Sentence Transformers**: Text embeddings

## Configuration

### Deal Threshold
Modify in `agents/planning_agent.py`:
```python
DEAL_THRESHOLD = 50  # Minimum discount in dollars
```

### RSS Feeds
Add/modify feeds in `agents/deals.py`:
```python
feeds = [
    "https://www.dealnews.com/c142/Electronics/?rss=1",
    # Add more feeds here
]
```

### Modal Container Settings
Keep containers warm in `pricer_service2.py`:
```python
MIN_CONTAINERS = 1  # Set to 1 to keep warm (costs credits)
```

## Performance

The ensemble approach typically achieves:
- RMSLE < 0.5
- Hit rate > 60% (within 20% or $40 of actual price)
- Response time: ~2-30 seconds depending on cold start

## Contributing

Community contributions are welcome! See the `community_contributions/` folder for examples of:
- XGBoost ensemble variations
- Alternative deployment strategies
- UI improvements

## Acknowledgments

Built as part of LLM Engineering Week 8 coursework.
