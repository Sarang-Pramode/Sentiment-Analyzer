from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi import Header
from fastapi import APIRouter


# initialize FastAPI router
router = APIRouter()

# Example model
class Item(BaseModel):
    """
    Item Model
    Attributes:
    name: str - The name of the item
    price: float - The price of the item
    quantity: int - The quantity of the item
    """
    name: str
    price: float
    quantity: int

# Example endpoint with path parameters
@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Example endpoint with query parameters
@router.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# Example endpoint with request body
@router.post("/items/")
def create_item(item: Item):
    return item

# Example endpoint with error handling
@router.get("/items/{item_id}/price")
def read_item_price(item_id: int):
    if item_id == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "price": 9.99}

# Example endpoint with path operation decorator
@router.put("/items/{item_id}")
@router.patch("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}

# Example endpoint with dependency injection
@router.get("/items/{item_id}/info")
def read_item_info(item_id: int, user_agent: str = Header(None)):
    return {"item_id": item_id, "user_agent": user_agent}

# Example endpoint with response model
@router.get("/items/{item_id}/name", response_model=Item)
def read_item_name(item_id: int):
    return {"name": "Example Item", "price": 9.99, "quantity": 10}