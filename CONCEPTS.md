# FastAPI Concepts Guide

## Core Concepts

### FastAPI
A Python web framework that uses type hints to automatically validate data, generate documentation, and handle errors. Instead of manually checking if data is valid, FastAPI does it for you based on type annotations like `: int` or `: str`.

### Decorators (`@app.get()`, `@app.post()`)
Special functions that modify the function below them. In FastAPI, they register URL endpoints:
- `@app.get("/items")` - handles GET requests to /items (reading data)
- `@app.post("/items")` - handles POST requests to /items (creating data)

### Type Hints
Python annotations that specify what type data should be (e.g., `name: str`, `age: int`). FastAPI uses these to:
1. Validate incoming data
2. Convert data to the correct type
3. Generate automatic documentation
4. Show errors when data is wrong

### Pydantic BaseModel
A class you inherit from to define data structures. FastAPI validates request data against these models automatically. If you expect JSON with `name` and `age`, you create a model with those fields.

### Path Parameters
Variables in URLs like `/items/{item_id}` where `{item_id}` can be any value. FastAPI extracts these automatically and validates their type based on your function signature.

### Request Body
Data sent with POST/PUT requests (usually JSON). FastAPI validates this against your Pydantic models and converts it to Python objects you can use directly.

## HTTP Methods

- **GET** - Read/retrieve data (like viewing a webpage)
- **POST** - Create new data (like submitting a form)
- **PUT** - Update existing data completely
- **DELETE** - Remove data
- **PATCH** - Update part of existing data

## What Your Code Does

1. **Import tools** - Get FastAPI and data validation tools
2. **Create app** - Make a FastAPI application instance
3. **Define models** - Specify what Item and User data looks like
4. **Create endpoints** - Set up 4 URL routes:
   - `GET /` - Returns "Hello World"
   - `GET /items/{item_id}` - Returns the item ID you provide
   - `POST /items` - Creates an item, calculates tax if provided
   - `POST /users` - Creates a user

## Why This Matters

Traditional frameworks require manual validation:
```python
# Manual way (Flask/Django)
item_id = request.args.get('item_id')
if not item_id or not item_id.isdigit():
    return {"error": "invalid"}, 400
item_id = int(item_id)
```

FastAPI does it automatically:
```python
# FastAPI way
def read_item(item_id: int):
    # item_id is already validated and converted
```

## Next Steps

**Async/Await** - Allows your API to handle multiple requests simultaneously without blocking. Essential when calling databases, external APIs, or AI services. Without it, your server waits idle instead of processing other requests.

**Uvicorn** - The server that runs your FastAPI app (like how Apache runs PHP). You start it with `uvicorn main:app --reload`.

**Interactive Docs** - Visit `http://127.0.0.1:8000/docs` when your app runs to see auto-generated API documentation where you can test endpoints.
