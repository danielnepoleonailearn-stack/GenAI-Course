from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
def display_welcomeMessage():
    return {"message": "Welcome to the FastAPI app!"}

@app.post("/items/{item_name}")
def create_item(item_name: str):
    return {"item_name": item_name}

@app.get("/items")
def read_items(item_name: str):
    return {"item_name": item_name}

@app.post("/itemsOrder")
def order_items(itemName: str = Form(), count: str = Form()):
    return {
        "Product": itemName,
        "No_of_items": count,
        "status": "Order Placed Successfully"
    }