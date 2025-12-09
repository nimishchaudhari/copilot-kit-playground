#!/usr/bin/env python3
"""
Simple AI Chat App using CopilotKit with MCP integration
"""

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from copilotkit import LangGraphAGUIAgent
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
        llm=llm,
        tools=[],
        system_message=system_prompt
    )
    
    return agent

# Create the chat agent
copilotkit_agent = None
try:
    chat_agent = create_chat_agent()
    
    # Create LangGraphAGUIAgent for CopilotKit (recommended over LangGraphAgent)
    copilotkit_agent = LangGraphAGUIAgent(
        name="chat_agent",
        description="A simple AI chat assistant",
        graph=chat_agent
    )
    
    print("✓ Chat agent created successfully")
    
except Exception as e:
    print(f"✗ Error creating chat agent: {e}")

# Initialize CopilotKit SDK
if copilotkit_agent is not None:
    sdk = CopilotKitSDK(
        agents=[copilotkit_agent]
    )
    
    # Add the CopilotKit endpoints to our app
    sdk.setup(app)
else:
    print("⚠ Chat agent not created, skipping CopilotKit setup")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Define routes
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# MCP Server Integration - Create an endpoint to start an MCP server
@app.get("/mcp-server")
async def start_mcp_server():
    """
    Start an MCP server that can be hosted locally.
    This endpoint would typically be used by the client to host an MCP server.
    """
    # In a real implementation, this would start an actual MCP server
    # For now, we'll just return a message indicating the capability
    return {
        "message": "MCP Server integration enabled",
        "status": "ready",
        "instructions": "To connect to an MCP server, use the CopilotKit client with MCP configuration"
    }

# MCP Client Integration - Create an endpoint to connect to MCP servers
@app.get("/mcp-connect")
async def connect_to_mcp_server():
    """
    Connect to an MCP server hosted on the client device.
    This endpoint would typically be used by the client to establish connections.
    """
    # In a real implementation, this would handle connecting to MCP servers
    # For now, we'll just return a message indicating the capability
    return {
        "message": "MCP Client integration enabled",
        "status": "ready",
        "instructions": "To connect to an MCP server, configure your CopilotKit client with MCP settings"
    }

if __name__ == "__main__":
    import uvicorn
    print("Starting CopilotKit Chat App with MCP Integration...")
    uvicorn.run(app, host="0.0.0.0", port=8000)