# Price Is Right Package - Distribution Contents

This folder contains all the files needed to run and deploy "The Price is Right" deal hunting agentic AI system.

## 📦 Package Contents

### Core Application Files
- `deal_agent_framework.py` - Main agent framework orchestrator
- `price_is_right.py` - Gradio UI application
- `price_is_right_final.py` - Alternative final version with additional features
- `items.py` - Data processing utilities for products
- `testing.py` - Testing framework with RMSLE metrics

### Modal Deployment Files
- `pricer_service.py` - Function-based Modal deployment
- `pricer_service2.py` - Class-based Modal deployment (with caching)
- `pricer_ephemeral.py` - Ephemeral Modal deployment for testing
- `hello.py` - Basic Modal example
- `llama.py` - Llama model example on Modal
- `keep_warm.py` - Script to keep Modal containers warm

### Agents Package (`agents/` folder)
- `agent.py` - Base agent class with logging
- `planning_agent.py` - Main orchestrator agent
- `scanner_agent.py` - RSS feed scraper agent
- `ensemble_agent.py` - Ensemble model coordinator
- `specialist_agent.py` - Fine-tuned Llama agent (Modal)
- `frontier_agent.py` - RAG agent (GPT-4o-mini + ChromaDB)
- `random_forest_agent.py` - Traditional ML agent
- `messaging_agent.py` - Alert/notification agent
- `deals.py` - Data models (Deal, Opportunity, etc.)
- `__init__.py` - Package initialization

### Configuration Files
- `requirements.txt` - Python dependencies
- `setup.py` - Package setup configuration
- `pyproject.toml` - Modern Python package metadata
- `MANIFEST.in` - Distribution file inclusion rules
- `.gitignore` - Git ignore rules
- `.env.example` - Environment variables template
- `README.md` - Complete project documentation

### Data Files
- `memory.json` - Persistent storage for discovered deals
- `__init__.py` - Package initialization file
- `log_utils.py` - Logging utilities

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd deal-hunter-ai
pip install -r requirements.txt
```

### 2. Set Up Environment Variables
```bash
# Copy the example file
cp .env.example .env

# Edit .env with your actual API keys
nano .env  # or use your preferred editor
```

Required variables:
- `OPENAI_API_KEY` - Your OpenAI API key
- Modal credentials (set up via `modal setup`)

### 3. Deploy to Modal
```bash
modal setup  # First time only
modal deploy pricer_service2.py
```

### 4. Run the Application
```bash
# Run the Gradio UI
python price_is_right.py

# Or run the agent framework directly
python deal_agent_framework.py
```

## 📋 Installation as Package

You can install this as a Python package:

```bash
# Development mode (editable)
pip install -e .

# Regular installation
pip install .
```

## 🔧 Configuration

### Deal Threshold
Edit `agents/planning_agent.py` line 13:
```python
DEAL_THRESHOLD = 50  # Minimum discount in dollars
```

### RSS Feeds
Edit `agents/deals.py` lines 10-16 to add/modify RSS feeds.

### Keep Modal Warm
Edit `pricer_service2.py` line 24:
```python
MIN_CONTAINERS = 1  # Set to 1 to keep warm (costs credits)
```

## 📊 What's NOT Included

These files are excluded (too large or environment-specific):
- Model weights (`.pkl` files) - will be generated when you train models
- ChromaDB database (`products_vectorstore/`) - will be created on first run
- Jupyter notebooks - available in parent directory
- Community contributions - available in parent directory
- `.env` file with secrets - you must create this yourself

## 🎯 Next Steps

1. **Set up credentials**: Configure all required API keys in `.env`
2. **Deploy Modal service**: Run `modal deploy pricer_service2.py`
3. **Test the system**: Run `python deal_agent_framework.py`
4. **Launch UI**: Run `python price_is_right.py`

## 🐛 Troubleshooting

- **Modal auth errors**: Run `modal token new` from command line
- **Missing model files**: Train models using the Jupyter notebooks
- **ChromaDB errors**: Ensure you have created the vector database
- **API errors**: Verify all API keys are correctly set in `.env`

## 📝 Notes

- Model `.pkl` files need to be trained before running the ensemble
- ChromaDB vector store needs to be populated with product embeddings
- Some features require paid API access (OpenAI, Modal GPU credits)
- Notification features are optional (Pushover/Twilio)

---

For detailed documentation, see `README.md`
For training models and full setup, refer to the Jupyter notebooks in the parent directory.
