from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/items/")
def read_item():
    return {"Items": ["Item1", "Item2", "Item3"]}

@app.get("/items/item_id/")
def read_item_by_id(item_id: int):
    return {"Item ID": item_id}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"User ID": user_id, "name": "Labeat"}

app.get("/items/")
def get_all_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    return {"item_id": item_id, "item_name": name, "item_name": price}

app.post("/items/")
def create_item(name: str, price: float):
    return {"item_name":name, "item_price": price}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} has been deleted."}
