from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()	# Creates application instance


# Pydantic models for request/response validation
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    name: str
    email: str
    age: int
    is_active: bool = True

@app.get("/") #@-decorator <_takes the function below and does something with it
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/items")
def create_item(item: Item):
    """Create a new item using BaseModel validation"""
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.post("/users")
def create_user(user: User):
    """Create a new user using BaseModel validation"""
    return {"created_user": user, "status": "success"}




	# Documentation:

# ============================================
# BEGINNER-FRIENDLY DEEP DIVE
# ============================================

# 1. **What Makes FastAPI Special: Type Hints Do the Work**
#    Look at line 10: `item_id: int`
#    This simple annotation automatically does THREE powerful things:
#
#    a) VALIDATES: If someone visits /items/hello, FastAPI automatically returns an error
#       {"detail": [{"msg": "value is not a valid integer"}]}
#
#    b) CONVERTS: The URL string "123" is automatically converted to Python integer 123
#
#    c) DOCUMENTS: Visit http://127.0.0.1:8000/docs and you'll see interactive documentation
#       showing that item_id must be an integer - generated automatically from your code!

# 2. **Compare: With vs Without FastAPI**
#
#    WITHOUT FastAPI (traditional Flask/Django style):
#    ```
#    def read_item(request):
#        item_id = request.args.get('item_id')      # Get parameter manually
#        if not item_id or not item_id.isdigit():   # Validate manually
#            return {"error": "item_id must be a number"}, 400
#        item_id = int(item_id)                     # Convert manually
#        return {"item_id": item_id}
#    ```
#
#    WITH FastAPI (what you see above):
#    ```
#    def read_item(item_id: int):
#        return {"item_id": item_id}
#    ```
#    FastAPI does all the validation, conversion, and error handling for you!

# 3. **This Scales to Complex Data Structures**
#    Later, when you need to handle JSON request bodies (like creating a user profile),
#    you'll use Pydantic models. Here's a preview:
#
#    ```
#    from pydantic import BaseModel, EmailStr
#
#    class User(BaseModel):
#        name: str
#        email: EmailStr  # Validates email format!
#        age: int
#        is_active: bool = True  # Default value
#
#    @app.post("/users")
#    def create_user(user: User):
#        return {"created_user": user}
#    ```
#
#    FastAPI will automatically:
#    - Validate all field types (name is string, age is int, etc.)
#    - Check email format is valid (user@example.com, not just "hello")
#    - Apply default values (is_active defaults to True if not provided)
#    - Return clear error messages for each field that fails validation


# 4. **What's Next: Async/Await (Day 2 Preview)**
#
#    The next step in your learning is understanding async/await.
#    This is crucial when your API needs to wait for external services:
#
#    - Calling Claude AI or OpenAI APIs (wait for LLM response)
#    - Querying databases (wait for database query)
#    - Making HTTP requests to other APIs (wait for response)
#
#    Without async: Your server FREEZES while waiting. If a request takes 3 seconds,
#    NO other users can use your API during those 3 seconds!
#
#    With async: Your server can handle 100+ requests simultaneously, each waiting
#    for their own responses without blocking others.
#
#    Example preview:
#    ```
#    @app.get("/ask-claude")
#    async def ask_claude(question: str):
#        response = await anthropic_client.messages.create(...)  # Non-blocking wait
#        return {"answer": response.content}
#    ```
#
#    The `async def` and `await` keywords make this possible!

# 6. **Key Concepts Glossary for Beginners**
#
#    - FastAPI: A modern Python web framework that uses type hints for automatic validation
#    - ASGI: Async standard that allows handling multiple requests simultaneously (unlike older WSGI)
#    - Uvicorn: The server that runs your FastAPI app (like a restaurant kitchen runs the restaurant)
#    - Type Hints: The `: int`, `: str` annotations that tell Python (and FastAPI) what type data should be
#    - Pydantic: Library that FastAPI uses to validate data structures (you'll use this for complex data)
#    - Endpoint: A specific URL path in your API (like /items/{item_id})
#    - Path Parameter: Variable in the URL (the {item_id} part that changes)
#
# Happy learning! Build small projects, break things, and learn by doing. 🚀

# POST: to create data.
# GET: to read data.
# PUT: to update data.
# DELETE: to delete data.

# @app.post()
# @app.put()
# @app.delete()
# And the more exotic ones:

# @app.options()
# @app.head()
# @app.patch()
# @app.trace()