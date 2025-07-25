# This is the entry point for our application.
from enum import Enum
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
async def single_product(product_id: int):
    return {"response": "Single Product"}


# POST Request
# Create Product
@app.post('/product')
async def create_product(new_product: dict):
    return {"response": "Product Created", "new product": new_product}


# PUT Request
# Update Complete Data
@app.put("/product/{product_id}")
async def complete_update_product(new_updated_product: dict, product_id: int):
    return {"response": "Complete Data Updated", "product_id": product_id, "new update poduct": new_updated_product}


# PATCH Request
@app.patch("/product/{product_id}")
async def partial_update_product(new_updated_product: dict, product_id: int):
    return {"response": "Partial Data Updated", "product_id": product_id, "new update poduct": new_updated_product}


# DELETE Request
@app.delete("/product/{product_id}")
async def delete_product(product_id: int):
    return {"response": "Product Deleted.", "product_id": product_id}


# # Path Parameters Predefined Values
# class ProductCategory(str, Enum):
#     books = "Books"
#     clothing = "Clothing"
#     electronics = "Electronics"


# @app.get("/products/{category}")
# async def get_products(category: ProductCategory):
#     return {"response": "Products fetched", "category": category}

# # Path Converter
# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"You requested file at path": file_path}


# # Single Query Parameter
# @app.get("/products_by_category")
# async def get_product_by_category(category: ProductCategory):
#     return {"status": "Ok", "category": category}


# # Multiple Query Parameter
# @app.get("/products_by_category")
# async def get_product_by_category(category: ProductCategory, limit: int):
#     return {"status": "Ok", "category": category, "limit": limit}


# # Default Query Parameter
# @app.get("/products_by_category")
# async def get_product_by_category(category: ProductCategory, limit: int=10):
#     return {"status": "Ok", "category": category, "limit": limit}


# # Optional Query Parameter
# @app.get("/products_by_category")
# async def get_product_by_category(limit: int, category: ProductCategory | None = None):
#     return {"status": "Ok", "category": category, "limit": limit}


# # Path and Query Parameter
# @app.get("/product/{year}")
# async def product(year: str, category: ProductCategory):
#     return {"status": "OK", "year": year, "category": category}
