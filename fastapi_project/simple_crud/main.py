# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict

# 1. Create a FastAPI instance
app = FastAPI(title="My Simple Items API")

# 2. Define a Pydantic Model for our Item
# This class defines the structure and data types for an Item.
# FastAPI uses Pydantic for data validation and serialization.
class Item(BaseModel):
    # 'id' will be assigned by the server, so it's Optional for creation
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    # 'completed' status, defaults to False if not provided
    completed: bool = False

# 3. In-memory "Database" (a Python dictionary)
# We'll simulate a database using a dictionary where keys are item IDs
# and values are Item objects.
# In a real application, this would be a database like PostgreSQL, SQLite, etc.
items_db: Dict[int, Item] = {}
next_id = 1 # Simple counter for assigning unique IDs

# --- CRUD Operations ---

# 4. CREATE Operation: Add a new Item (HTTP POST)
@app.post("/items/", response_model=Item, status_code=201) # 201 Created status
async def create_item(item: Item):
    """
    Create a new item.
    The item ID will be automatically assigned.
    """
    global next_id # We need to modify the global next_id counter
    item.id = next_id # Assign a unique ID to the new item
    items_db[next_id] = item # Store the item in our in-memory database
    next_id += 1 # Increment the counter for the next item
    return item # Return the created item (with its new ID)

# 5. READ Operation: Get all Items (HTTP GET)
@app.get("/items/", response_model=List[Item])
async def read_items():
    """
    Retrieve a list of all items.
    """
    # Convert dictionary values to a list to return all items
    return list(items_db.values())

# 6. READ Operation: Get a single Item by ID (HTTP GET with Path Parameter)
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    """
    Retrieve a single item by its ID.
    Raises a 404 error if the item is not found.
    """
    # Check if the item exists in our database
    item = items_db.get(item_id)
    if item is None:
        # If not found, raise an HTTPException with status code 404
        raise HTTPException(status_code=404, detail="Item not found")
    return item # Return the found item

# 7. UPDATE Operation: Update an existing Item (HTTP PUT)
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    """
    Update an existing item by its ID.
    Raises a 404 error if the item is not found.
    """
    # Check if the item exists
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    # Update the item's properties
    # We assign the original ID to the updated_item to ensure consistency
    updated_item.id = item_id
    items_db[item_id] = updated_item
    return updated_item # Return the updated item

# 8. DELETE Operation: Remove an Item (HTTP DELETE)
@app.delete("/items/{item_id}", status_code=204) # 204 No Content for successful deletion
async def delete_item(item_id: int):
    """
    Delete an item by its ID.
    Raises a 404 error if the item is not found.
    """
    # Check if the item exists before attempting to delete
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    del items_db[item_id] # Remove the item from our database
    # For a 204 status code, you typically don't return any content.
    # FastAPI handles this automatically when status_code=204 is set.
    return