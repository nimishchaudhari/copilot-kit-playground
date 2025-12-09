#!/usr/bin/env python3
"""
Simple AI Chat App using CopilotKit
"""

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from copilotkit import LangGraphAgent
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from copilotkit.sdk import CopilotKitSDK
import os

# Create FastAPI app
app = FastAPI(title="CopilotKit Chat App")

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

# Create a simple chat agent
def create_chat_agent():
    """Create a basic chat agent"""
    
    # Define a simple prompt for the chat agent
    system_prompt = """
    You are a helpful AI assistant. Answer questions clearly and concisely.
    Keep responses brief but informative.
    """
    
    # Create a simple reactive agent
    agent = create_react_agent(
        model=llm,
        tools=[],
        prompt=system_prompt
    )
    
    return agent

# Create the chat agent
try:
    chat_agent = create_chat_agent()
    
    # Create LangGraphAgent for CopilotKit
    copilotkit_agent = LangGraphAgent(
        name="chat_agent",
        description="A simple AI chat assistant",
        graph=chat_agent
    )
    
    print("✓ Chat agent created successfully")
    
except Exception as e:
    print(f"✗ Error creating chat agent: {e}")
    # Exit if we can't create the agent
    exit(1)

# Initialize CopilotKit SDK
sdk = CopilotKitSDK(
    agents=[copilotkit_agent]
)

# Add the CopilotKit endpoints to our app
sdk.setup(app)

# Setup templates
templates = Jinja2Templates(directory="templates")

# Define routes
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    print("Starting CopilotKit Chat App...")
    uvicorn.run(app, host="0.0.0.0", port=8000)