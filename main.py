from fastapi import FastAPI, HTTPException

app = FastAPI()

items = []

@app.get("/")
def home():
    return {"message": "Welcome to CRUD API"}

# CREATE
@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return {
        "message": "Item created",
        "item": item
    }

# READ ALL
@app.get("/items")
def get_items():
    return items

# READ ONE
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

# UPDATE
@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")

    items[item_id] = item
    return {
        "message": "Item updated",
        "item": item
    }

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")

    deleted = items.pop(item_id)

    return {
        "message": "Item deleted",
        "item": deleted
    }