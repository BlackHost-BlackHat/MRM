from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

# Create FastAPI application
app = FastAPI()


# Data models for validation
class Item(BaseModel): #build object schema
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    name: str
    email: str
    age: int
    is_active: bool = True

class ChatRequests(BaseModel):
    message: str
    temperature: float=0.7
    
@app.get("/")  # Keep one
def read_root():
    return {"message": "Hello World"}

@app.get("/health", response_class=PlainTextResponse)
def health_check():
    return "OK"

@app.get("/custom")
def custom_response():
    return JSONResponse(
        content={"status": "success"},
        status_code=201,
        headers={"X-Custom-Header": "value"}
    )

@app.post("/items")  # Keep one
def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        item_dict["price_with_tax"] = item.price + item.tax
    return item_dict

@app.post("/chat")  # Different route!
def create_chat(item: ChatRequests):
    return {"received": item.message, "temp": item.temperature}

@app.post("/users")
def create_user(user: User):
    return {"created_user": user, "status": "success"}

@app.get("/search/")
def search_items(q: str, max_results: int = 10):
    return {"query": q, "limit": max_results}