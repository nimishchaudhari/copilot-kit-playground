# CopilotKit Chat App

A simple AI chat application using CopilotKit and LangGraph.

## Features

- Web-based chat interface
- AI assistant powered by OpenAI GPT
- Direct-to-LLM integration with CopilotKit
- FastAPI backend with LangGraph agent

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your OpenAI API key (required):
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

3. Run the application:
   ```bash
   python chat_app.py
   ```

4. Visit `http://localhost:8000` in your browser to use the chat app

## Architecture

This application uses:
- **FastAPI** for the web framework
- **CopilotKit** for AI agent integration
- **LangGraph** for building reactive agents
- **LangChain** for LLM integration
- **OpenAI GPT-4o** as the language model

## Files

- `chat_app.py` - Main application with FastAPI and CopilotKit setup
- `requirements.txt` - Python dependencies
- `templates/index.html` - Simple chat UI
