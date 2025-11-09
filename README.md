---
title: Streamlit Uvicorn Chatbot
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: "1.28.0"
app_file: src/ui/app.py
pinned: false
---

# LLM Learning Project

A learning project exploring LLM integration with different frameworks: FastAPI and Streamlit.

## Project Structure

```
llm-learning/
├── src/
│   ├── api/          # FastAPI backend with Claude AI integration
│   │   └── main.py   # Chat API endpoint
│   └── ui/           # Streamlit frontend
│       └── app.py    # Interactive chatbot UI
├── CONCEPTS.md       # FastAPI learning notes
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Features

### FastAPI Chat API (`src/api/main.py`)
- RESTful chat endpoint using Claude AI
- Pydantic model validation
- Async support for concurrent requests
- Auto-generated API documentation

### Streamlit Chatbot (`src/ui/app.py`)
- Interactive chat interface
- Session state management
- Real-time streaming responses
- Deployed on Hugging Face Spaces

## Setup

1. **Install dependencies:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Configure environment variables:**
Create a `.env` file:
```
ANTHROPIC_API_KEY=your_api_key_here
```

3. **Run the FastAPI backend:**
```bash
uvicorn src.api.main:app --reload
```
Visit:
- http://127.0.0.1:8000/docs - Interactive API docs
- http://127.0.0.1:8000/chat - Chat endpoint

4. **Run the Streamlit UI:**
```bash
streamlit run src/ui/app.py
```

## Deployment

This project is deployed on Hugging Face Spaces. The Streamlit app runs automatically when pushed to the HF Space repository.

## Learning Resources

See [CONCEPTS.md](CONCEPTS.md) for FastAPI core concepts and learning notes.
