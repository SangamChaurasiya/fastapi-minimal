# This is the entry point for our application.
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello from FastAPI"}


# GET Request
# Read or Fetch All Data
@app.get("/products")
async def all_products():
    return {"response": "All Products"}


# Read or Fetch Single Data
@app.get("/product/{product_id}")
def single_product(product_id: int):
    return {"response": "Single Product"}


# POST Request
# Create Product
@app.post('/product')
def create_product(new_product: dict):
    return {"response": "Product Created", "new product": new_product}


# PUT Request
# Update Complete Data
@app.put("/product/{product_id}")
def complete_update_product(new_updated_product: dict, product_id: int):
    return {"response": "Complete Data Updated", "product_id": product_id, "new update poduct": new_updated_product}


# PATCH Request
@app.patch("/product/{product_id}")
def partial_update_product(new_updated_product: dict, product_id: int):
    return {"response": "Partial Data Updated", "product_id": product_id, "new update poduct": new_updated_product}


# DELETE Request
@app.delete("/product/{product_id}")
def delete_product(product_id: int):
    return {"response": "Product Deleted.", "product_id": product_id}
