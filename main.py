# This is the entry point for our application.
from enum import Enum
from fastapi import FastAPI, status, Query, Path
from typing import Annotated
from pydantic import AfterValidator


app = FastAPI()


# @app.get("/")
# async def home():
#     return {"message": "Hello from FastAPI"}

# # GET Request
# # Read or Fetch All Data
# @app.get("/products")
# async def all_products():
#     return {"response": "All Products"}

# # Read or Fetch Single Data
# @app.get("/product/{product_id}", status_code=status.HTTP_200_OK)
# async def single_product(product_id: int):
#     return {"response": "Single Product"}

# # POST Request
# # Create Product
# @app.post('/product', status_code=status.HTTP_201_CREATED)
# async def create_product(new_product: dict):
#     return {"response": "Product Created", "new product": new_product}

# # PUT Request
# # Update Complete Data
# @app.put("/product/{product_id}", status_code=status.HTTP_200_OK)
# async def complete_update_product(new_updated_product: dict, product_id: int):
#     return {"response": "Complete Data Updated", "product_id": product_id, "new update poduct": new_updated_product}

# # PATCH Request
# @app.patch("/product/{product_id}", status_code=status.HTTP_200_OK)
# async def partial_update_product(new_updated_product: dict, product_id: int):
#     return {"response": "Partial Data Updated", "product_id": product_id, "new update poduct": new_updated_product}

# # DELETE Request
# @app.delete("/product/{product_id}", status_code=status.HTTP_200_OK)
# async def delete_product(product_id: int):
#     return {"response": "Product Deleted.", "product_id": product_id}

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

PRODUCTS = [
    {
        "id": 1,
        "title": "Fjallraven - Foldstack No. 1 Backpack, Fits 15 Laptops",
        "price": 109.95,
        "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday"
    },
    {
        "id": 2,
        "title": "Mens Casual Premium Slim Fit T-Shirts",
        "price": 22.3,
        "description": "Slim-fitting style, contrast raglan long sleeve, three button henley placket, light weight & soft fabric for breathable and comfortable wearing. And solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket."
    },
    {
        "id": 3,
        "title": "Mens Cotton Jacket",
        "price": 55.99,
        "description": "Great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, travelling or other outdoors. Good gift choice for you and your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day."
    },
]

# @app.get("/products")
# async def get_products(search: str | None = Query(default=None, max_length=5, pattern="^[a-z]+$")):
#     if search:
#         search = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS

# # Validation with Annotated
# @app.get("/products")
# async def get_products(
#     search: 
#         Annotated[
#             str | None, 
#             Query(default=None, 
#                   max_length=5)
#                   ] = None):
#     if search:
#         search = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS

# # Multiple Search Terms (List)
# @app.get("/products")
# async def get_products(search: Annotated[list[str] | None, Query()] = None):
#     if search:
#         filtered_products = []
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS

# # Alias Parameters
# @app.get("/products")
# async def get_products(search: str | None = Query(alias="q", description="Search by Product Title")):
#     if search:
#         search = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS

# # Deprecating Parameters
# @app.get("/products")
# async def get_products(search: str | None = Query(deprecated=True)):
#     if search:
#         search = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS


# # Custom Validation
# def check_valid_id(id: str):
#     if not id.startswith("prod-"):
#         raise ValueError("ID must start with 'prod-'")
#     return id

# @app.get("/products")
# async def get_products(id: Annotated[str | None, AfterValidator(check_valid_id)]=None):
#     if id:
#         return {"id": id, "message": "Valid product ID"}
#     return {"message": "No ID provided"}


# # Basic Path Parameter
# @app.get("/products/{product_id}")
# async def get_product(product_id: int):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             return product
#     return {"error": "Product not found"}

# # Numeric Validation for Path Parameter
# @app.get("/products/{product_id}")
# async def get_product(product_id: Annotated[int, Path(ge=1)]):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             return product
#     return {"error": "Product not found"}

# # Adding Metadata with Path
# @app.get("/products/{product_id}")
# async def get_product(product_id: Annotated[int, Path(title="The ID of the product", description="This is Product ID")]):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             return product
#     return {"error": "Product not found"}

# Combining Path and Query Parameter
@app.get("/products/{product_id}")
async def get_product(product_id: Annotated[int, Path(gt=0, le=100)], search: Annotated[str|None, Query(max_length=20)] = None):
    for product in PRODUCTS:
        if product["id"] == product_id:
            if search and search.lower() not in product["title"].lower():
                return {"error": "Product does not match search term"}
            return product
    return {"error": "Product not found"}
