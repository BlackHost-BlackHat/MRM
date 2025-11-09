from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from anthropic import Anthropic
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


class Message(BaseModel):
    """
    Represents a single chat message.
    Pydantic automatically validates that incoming JSON has these exact fields.
    """
    role: str      # "user" or "assistant" - who sent the message
    content: str   # The actual message text


class ChatRequests(BaseModel):
    """
    Represents the full chat request body.
    Expects a list of Message objects.
    Example JSON:
    {
        "messages": [
            {"role": "user", "content": "Hello!"}
        ]
    }
    """
    messages: List[Message]


@app.post("/chat")
async def chat(request: ChatRequests):
    """
    Chat endpoint that receives messages and returns Claude AI responses.

    Flow:
    1. Receives validated ChatRequests (FastAPI + Pydantic handle validation)
    2. Converts Pydantic models to dictionaries for Anthropic API
    3. Sends messages to Claude AI
    4. Returns Claude's response as JSON
    """

    # Convert Pydantic Message objects to dictionaries
    messages = [{"role": m.role, "content": m.content}
                for m in request.messages]

    # Send request to Claude AI via Anthropic SDK
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=messages
    )

    # Extract text from response and return as JSON
    return {"response": response.content[0].text}
