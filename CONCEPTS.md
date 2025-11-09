# LLM Learning Project - Complete Beginner's Guide

This guide explains every part of the code in simple terms. Think of it as your programming dictionary!

---

## Table of Contents
1. [FastAPI Backend (`src/api/main.py`)](#fastapi-backend)
2. [Streamlit UI (`src/ui/app.py`)](#streamlit-ui)
3. [Core Concepts Dictionary](#core-concepts-dictionary)

---

# FastAPI Backend (`src/api/main.py`)

## What Does This File Do?
Creates a web API that receives chat messages and sends them to Claude AI. It's like a middleman between your app and Claude.

## Line-by-Line Explanation

### Imports (Lines 1-6)
```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from anthropic import Anthropic
import os
from dotenv import load_dotenv
```

**What's happening:**
- `fastapi` - The web framework that creates your API
- `pydantic` - Checks that data is correct (like spell-check for data)
- `typing.List` - Says "this will be a list of things"
- `anthropic` - The library to talk to Claude AI
- `os` - Reads environment variables (like your API key)
- `dotenv` - Loads your `.env` file where secrets are stored

**Why we need this:**
Think of imports like getting tools from a toolbox before starting work.

### Load API Key (Lines 8-11)
```python
load_dotenv()

app = FastAPI()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
```

**What's happening:**
1. `load_dotenv()` - Reads your `.env` file
2. `app = FastAPI()` - Creates your web application
3. `client = Anthropic(...)` - Creates connection to Claude AI using your API key

**Real-world analogy:**
- `.env` file = Your keychain with all your passwords
- `load_dotenv()` = Getting the right key from the keychain
- `app` = Opening your shop for business
- `client` = Your phone line to Claude AI

### Data Models (Lines 14-34)

#### Message Model (Lines 14-20)
```python
class Message(BaseModel):
    role: str      # "user" or "assistant"
    content: str   # The actual message text
```

**What's happening:**
Defines what a single message looks like. Every message must have:
- `role` - Who said it ("user" or "assistant")
- `content` - What they said

**Real-world analogy:**
Like a text message bubble on your phone:
- Role = Name at the top (You or Friend)
- Content = The message text

#### ChatRequests Model (Lines 23-34)
```python
class ChatRequests(BaseModel):
    messages: List[Message]
```

**What's happening:**
Says "a chat request is a list of Message objects"

**Example JSON this expects:**
```json
{
  "messages": [
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi there!"},
    {"role": "user", "content": "How are you?"}
  ]
}
```

**Real-world analogy:**
Like your entire WhatsApp chat history with one person.

### The Chat Endpoint (Lines 37-61)
```python
@app.post("/chat")
async def chat(request: ChatRequests):
```

**What's happening:**
- `@app.post("/chat")` - Creates a URL endpoint at `/chat` that accepts POST requests
- `async def` - Function can handle multiple requests at once
- `request: ChatRequests` - Expects data matching our ChatRequests model

**Real-world analogy:**
Like setting up a specific phone number (the `/chat` endpoint) where people can call to talk to Claude.

#### Inside the Function (Lines 49-61)
```python
# Convert Pydantic Message objects to dictionaries
messages = [{"role": m.role, "content": m.content}
            for m in request.messages]
```
**What's happening:**
Transforms the data from Pydantic format to plain Python dictionaries that the Anthropic API understands.

**Before (Pydantic):** `Message(role="user", content="Hi")`
**After (Dict):** `{"role": "user", "content": "Hi"}`

```python
# Send request to Claude AI
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=messages
)
```
**What's happening:**
- Calls Claude AI with the conversation history
- `model` - Which version of Claude to use
- `max_tokens` - Maximum length of response (roughly 750 words)
- `messages` - The conversation history

```python
# Extract text from response and return as JSON
return {"response": response.content[0].text}
```
**What's happening:**
Gets Claude's text response and wraps it in JSON format to send back.

**Example return:**
```json
{
  "response": "Hello! I'm doing well, thank you for asking..."
}
```

---

# Streamlit UI (`src/ui/app.py`)

## What Does This File Do?
Creates an interactive chat interface in your web browser. It's the visual part users interact with.

## Line-by-Line Explanation

### Imports (Lines 1-4)
```python
import streamlit as st
from anthropic import Anthropic
import os
from dotenv import load_dotenv
```

**What's happening:**
- `streamlit` - Creates web UIs with simple Python code
- `anthropic` - Direct connection to Claude (no FastAPI middleman here!)
- `os` & `dotenv` - Same as before, for loading API keys

### Setup (Lines 6-9)
```python
load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

st.title("Simple Chatbot")
```

**What's happening:**
1. Load API key from `.env`
2. Connect to Claude AI
3. Display "Simple Chatbot" as the page title

**Real-world analogy:**
Opening a chat app and seeing the title at the top.

### Session State (Lines 11-12)
```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

**What's happening:**
Checks if we've stored messages before. If not, create an empty list.

**What is `st.session_state`?**
It's Streamlit's memory. Without it, the page would forget everything every time you type a message!

**Real-world analogy:**
Like your brain remembering a conversation. Without session state, you'd forget what you just said (like the movie "Memento").

### Display Chat History (Lines 14-17)
```python
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
```

**What's happening:**
Loop through all saved messages and display them.

**Step by step:**
1. `for message in ...` - Look at each message one by one
2. `with st.chat_message(message["role"])` - Create a chat bubble (user or assistant style)
3. `st.markdown(message["content"])` - Put the text inside the bubble

**Real-world analogy:**
When you open WhatsApp, it shows all previous messages. This is doing the same thing.

### Handle New Messages (Lines 19-37)
```python
if prompt := st.chat_input("What's up?"):
```

**What's happening:**
- `st.chat_input("What's up?")` - Shows a text box at the bottom
- `:=` - "Walrus operator" - assigns AND checks if there's a value
- Only runs the code inside if user typed something

**Think of it as:**
"If the user typed something, save it as `prompt` and run this code"

#### Add User Message (Lines 21-24)
```python
st.session_state.messages.append({"role": "user", "content": prompt})
with st.chat_message("user"):
    st.markdown(prompt)
```

**What's happening:**
1. Save the user's message to memory
2. Display it on screen immediately

**Why do both?**
- `append()` = Save for later (like writing in a diary)
- `st.chat_message()` = Show on screen now (like speaking out loud)

#### Get AI Response (Lines 26-32)
```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=st.session_state.messages
)
assistant_message = response.content[0].text
```

**What's happening:**
1. Send entire conversation history to Claude
2. Claude reads everything and generates a response
3. Extract just the text from Claude's response

**Real-world analogy:**
Like sending a text message and waiting for a reply.

#### Add Assistant Message (Lines 34-37)
```python
st.session_state.messages.append({"role": "assistant", "content": assistant_message})
with st.chat_message("assistant"):
    st.markdown(assistant_message)
```

**What's happening:**
Same as user message, but for Claude's response:
1. Save to memory
2. Display on screen

---

# Core Concepts Dictionary

## FastAPI Concepts

### What is an API?
**Application Programming Interface** - A way for programs to talk to each other.

**Real-world analogy:**
A restaurant menu. You (the customer) don't go into the kitchen. You look at the menu (API) and order. The kitchen (backend) makes your food and brings it back.

### HTTP Methods
- **GET** - "Give me information" (like viewing a webpage)
- **POST** - "Here's new information, process it" (like submitting a form)
- **PUT** - "Update this information"
- **DELETE** - "Remove this"

**Real-world analogy:**
- GET = Asking "What's on the menu?"
- POST = Placing an order
- PUT = Changing your order
- DELETE = Canceling your order

### Decorators (`@app.post("/chat")`)
Special Python syntax that modifies the function below it.

**What `@app.post("/chat")` means:**
"When someone sends a POST request to `/chat`, run this function"

**Real-world analogy:**
A sign on a door saying "Ring doorbell for deliveries" - tells people what to do.

### Async/Await
Lets your program do multiple things at once instead of waiting.

**Without async:**
Customer 1 orders → Wait for food → Serve Customer 1 → Customer 2 orders → Wait for food → Serve Customer 2

**With async:**
Customer 1 orders → Customer 2 orders → Customer 3 orders → Serve all when ready

### Type Hints (`role: str`)
Tell Python what type of data to expect.

```python
def greet(name: str) -> str:
    return f"Hello {name}"
```

- `name: str` - expects text (string)
- `-> str` - returns text (string)

**Why?**
Catches errors before they happen. Like spell-check for code!

### Pydantic BaseModel
Automatically validates data and shows nice error messages.

**Without Pydantic:**
```python
if "role" not in data:
    return error("Missing role")
if not isinstance(data["role"], str):
    return error("Role must be string")
# ... many more checks
```

**With Pydantic:**
```python
class Message(BaseModel):
    role: str
    content: str
# All validation automatic!
```

## Streamlit Concepts

### What is Streamlit?
A Python library that turns scripts into interactive web apps with minimal code.

**Without Streamlit (Flask/React):**
- Write HTML
- Write CSS
- Write JavaScript
- Set up routes
- Handle state
- ~500+ lines of code

**With Streamlit:**
- Write Python
- ~38 lines of code (like our app.py!)

### Session State
Streamlit's way of remembering data between interactions.

**The Problem:**
Streamlit reruns your entire script every time you interact with it. Without session state, it would forget everything!

**Example:**
```python
# BAD - Gets reset to 0 every time
count = 0
if st.button("Click me"):
    count += 1  # Will always be 1!

# GOOD - Remembers across reruns
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Click me"):
    st.session_state.count += 1  # Actually increases!
```

### Widgets
Interactive elements users can interact with:

- `st.text_input()` - Text box
- `st.button()` - Clickable button
- `st.slider()` - Slider control
- `st.chat_input()` - Chat input box
- `st.chat_message()` - Chat bubble

**Real-world analogy:**
Like HTML elements (`<input>`, `<button>`) but written in Python!

### Walrus Operator (`:=`)
Assigns a value AND checks if it exists in one line.

**Without walrus:**
```python
prompt = st.chat_input("What's up?")
if prompt:
    # use prompt
```

**With walrus:**
```python
if prompt := st.chat_input("What's up?"):
    # use prompt
```

Does the same thing, just shorter!

## Environment Variables

### What is a `.env` file?
A file that stores secret information (like passwords and API keys) that shouldn't be in your code.

**Example `.env`:**
```
ANTHROPIC_API_KEY=sk-ant-xxxxx
DATABASE_PASSWORD=secret123
```

### Why use `.env`?
1. **Security** - Don't upload secrets to GitHub
2. **Flexibility** - Different keys for development vs production
3. **Sharing** - Share code without sharing secrets

**How it works:**
1. `.gitignore` includes `.env` (so it's not uploaded)
2. `load_dotenv()` reads it
3. `os.getenv("KEY_NAME")` gets the value

## AI/LLM Concepts

### What is Claude?
An AI assistant made by Anthropic. It reads text and generates intelligent responses.

### Model Names (`claude-sonnet-4-20250514`)
Different versions of Claude with different capabilities:
- **Opus** - Most powerful, slower, more expensive
- **Sonnet** - Balanced (what we use)
- **Haiku** - Fastest, cheaper, less powerful

### Tokens
How AI models measure text. Roughly:
- 1 token ≈ 0.75 words
- 1024 tokens ≈ 750 words

`max_tokens=1024` means "response can be up to ~750 words"

### Messages Format
Claude expects messages in this format:
```python
[
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi there!"},
    {"role": "user", "content": "How are you?"}
]
```

**Why this format?**
Claude needs to know who said what to understand context and maintain conversation flow.

---

## Common Beginner Questions

### Q: Why do we need both FastAPI and Streamlit versions?
**A:** They serve different purposes:
- **FastAPI** (`src/api/main.py`) - For building APIs that other programs can use
- **Streamlit** (`src/ui/app.py`) - For building user-facing web interfaces

Think of FastAPI as a kitchen (backend) and Streamlit as the dining room (frontend).

### Q: What's the difference between `async` and regular functions?
**A:**
- **Regular function:** Makes you wait for each task to finish
- **Async function:** Can juggle multiple tasks at once

Like a chef cooking multiple dishes simultaneously vs one at a time.

### Q: Why use Pydantic models?
**A:** Automatic data validation! Instead of writing 50 lines checking if data is valid, Pydantic does it automatically and gives helpful error messages.

### Q: What happens if my API key is wrong?
**A:** You'll get an authentication error. The Anthropic client will tell you the key is invalid.

### Q: How does Streamlit remember my chat history?
**A:** Using `st.session_state` - Streamlit's memory system that persists between reruns.

### Q: Can I use this code for other AI models?
**A:** Yes! You'd just need to:
1. Change the `anthropic` library to whatever the AI provider uses
2. Update the API call format
3. Keep the rest of the structure the same

---

## Next Steps for Learning

1. **Try modifying the code:**
   - Change the title
   - Add a custom greeting
   - Adjust `max_tokens` to see what happens

2. **Add features:**
   - Button to clear chat history
   - Temperature slider (controls randomness)
   - Character counter

3. **Learn more about:**
   - FastAPI documentation: https://fastapi.tiangolo.com/
   - Streamlit documentation: https://docs.streamlit.io/
   - Anthropic API: https://docs.anthropic.com/

4. **Experiment safely:**
   - The code won't break anything
   - You can always restore from Git
   - Try things and see what happens!

---

## Troubleshooting

### "Module not found" error
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### "API key not found" error
**Solution:** Create `.env` file with your API key
```
ANTHROPIC_API_KEY=your_key_here
```

### Streamlit page is blank
**Solution:** Check terminal for errors, make sure `.env` file exists

### FastAPI shows 422 error
**Solution:** Your request format is wrong. Check that JSON matches the Pydantic models.

---

**Remember:** Everyone was a beginner once. Take it slow, experiment, and don't be afraid to break things. That's how you learn! 🚀
