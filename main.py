# This is the entry point for our application.
from enum import Enum
from fastapi import FastAPI, status, Query, Path, Body, Cookie
from typing import Annotated
from pydantic import AfterValidator, BaseModel, Field


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

# # Combining Path and Query Parameter
# @app.get("/products/{product_id}")
# async def get_product(product_id: Annotated[int, Path(gt=0, le=100)], search: Annotated[str|None, Query(max_length=20)] = None):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             if search and search.lower() not in product["title"].lower():
#                 return {"error": "Product does not match search term"}
#             return product
#     return {"error": "Product not found"}

# ---------------------------------------------------------------

# # Without Pydantic
# # Create or Insert Data
# @app.post("/product")
# async def create_product(new_product: dict):
#     return new_product


# # With Pydantic
# # Define the Product model
# class Product(BaseModel):
#     id: int
#     name: str
#     price: float
#     stock: int | None = None


# @app.post("/product")
# async def create_product(new_product: Product):
#     return new_product

# # Add new calculated attribute
# @app.post("/product")
# async def create_product(new_product: Product):
#     product_dict = new_product.model_dump()
#     price_with_tax = new_product.price * 1.18
#     product_dict.update({"price_with_tax": price_with_tax})
#     return product_dict

# # Combining Request Body with Path Parameters
# @app.put("/products/{product_id}")
# async def update_product(product_id: int, new_updated_product: Product):
#     return {"product_id": product_id,
#             "new_updated_product": new_updated_product}

# # Adding Query Parameters
# @app.put("/products/{product_id}")
# async def update_product(product_id: int, new_updated_product: Product, discount: float | None = None):
#     return {"product_id": product_id, "new_updated_product": new_updated_product, "discount": discount}

# ---------------------------------------------------------------

# Multiple Body Parameters
class Product(BaseModel):
    name: str
    price: float
    stock: int | None = None

class Seller(BaseModel):
    username : str
    fullname : str | None = None

# @app.post("/product")
# async def create_product(product: Product, seller: Seller):
#     return {"product": product, "seller": seller}

# # Make body optional
# @app.post("/product")
# async def create_product(product: Product, seller: Seller | None = None):
#     return {"product": product, "seller": seller}

# # Singular values in body
# @app.post("/product")
# async def create_product(product: Product, seller: Seller, sec_key: Annotated[str, Body()]):
#     return {"product": product, "seller": seller, "sec_key": sec_key}

# Embed a single body parameter
# # Without Embed
# @app.post("/product")
# async def create_product(product: Product):
#     return product

# # With Embed
# @app.post("/product")
# async def create_product(product: Annotated[Product, Body(embed=True)]):
#     return product

# ---------------------------------------------------------------

# # Pydantic's Field
# class Product(BaseModel):
#     name: str = Field(
#         title="Product Name",
#         description="The name of the product",
#         max_length=100,
#         min_length=3,
#         pattern="^[A-Za-z0-9]+$"
#     )
#     price: float = Field(
#         gt=0,
#         title="Product Price",
#         description="The price of the product in USD, must be greater than zero"
#     )
#     stock: int | None = Field(
#         default=None,
#         ge=0,
#         title="Stock Qunatity",
#         description="The number of items in stock, must be non-negative."
#     )

# @app.post("/product")
# async def create_product(product: Product):
#     return product

# ---------------------------------------------------------------

# # Nested Body Models
# # Submodel
# class Category(BaseModel):
#     name: str = Field(
#         title="Category Name",
#         description="The name of the product company",
#         max_length=50,
#         min_length=1
#     )
#     description: str | None = Field(
#         default=None,
#         title="Category Description",
#         description="A brief description of the category",
#         max_length=200
#     )

# # Model which will use Submodel
# class Product(BaseModel):
#     category: Category | None = Field(
#         default=None,
#         title="Product Category",
#         description="The category to which the product belongs"
#     )
#     name: str = Field(
#         title="Product Name",
#         description="The name of the product",
#         max_length=100,
#         min_length=3,
#         pattern="^[A-Za-z0-9]+$"
#     )
#     price: float = Field(
#         gt=0,
#         title="Product Price",
#         description="The price of the product in USD, must be greater than zero"
#     )
#     stock: int | None = Field(
#         default=None,
#         ge=0,
#         title="Stock Qunatity",
#         description="The number of items in stock, must be non-negative."
#     )

# @app.post("/product")
# async def create_product(product: Product):
#     return product

# ---------------------------------------------------------------

# # Attributes with lists of submodels
# class Category(BaseModel):
#     name: str = Field(
#         title="Category Name",
#         description="The name of the product company",
#         max_length=50,
#         min_length=1
#     )
#     description: str | None = Field(
#         default=None,
#         title="Category Description",
#         description="A brief description of the category",
#         max_length=200
#     )

# class Product(BaseModel):
#     category: list[Category] | None = Field(
#         default=None,
#         title="Product Category",
#         description="The category to which the product belongs"
#     )
#     name: str = Field(
#         title="Product Name",
#         description="The name of the product",
#         max_length=100,
#         min_length=3,
#         pattern="^[A-Za-z0-9]+$"
#     )
#     price: float = Field(
#         gt=0,
#         title="Product Price",
#         description="The price of the product in USD, must be greater than zero"
#     )
#     stock: int | None = Field(
#         default=None,
#         ge=0,
#         title="Stock Qunatity",
#         description="The number of items in stock, must be non-negative."
#     )

# @app.post("/product")
# async def create_product(product: Product):
#     return product

# ---------------------------------------------------------------

# # using Field-level examples
# class Product(BaseModel):
#     name: str = Field(examples=["Moto E"])
#     price: float = Field(examples=[23.56])
#     stock: int | None = Field(default=None, examples=[23])

# @app.post("/products")
# async def create_product(product: Product):
#     return product

# # Using Pydantic's json_schema_extra
# class Product(BaseModel):
#     name: str
#     price: float
#     stock: int | None = None

#     model_config = {
#         "json_schema_extra": {
#             "examples": [
#                 {
#                     "name": "Moto E",
#                     "price": 34.56,
#                     "stock": 20
#                 }
#             ]
#         }
#     }

# @app.post("/products")
# async def create_product(product: Product):
#     return product

# ---------------------------------------------------------------

# # Cookie Parameter
# @app.get("/product/recommendations")
# async def get_recommendations(session_id: Annotated[str | None, Cookie()] = None):
#     if session_id:
#         return {"message": f"Recommendations for session {session_id}", "session_id": session_id}
#     return {"message": "No session ID provided, showing default recommendations"}

# # # To test the above API the following command in the terminal:
# # curl -H "Cookie: session_id=abc123" http://127.0.0.1:8000/product/recommendations
# # {"message":"Recommendations for session abc123","session_id":"abc123"}

# ---------------------------------------------------------------

# # Cookie parameter with Pydantic Model
# class ProductCookies(BaseModel):
#     session_id: str
#     preferred_category: str | None = None
#     tracking_id: str | None = None


# @app.get("/products/recommendations")
# async def get_recommendations(cookies: Annotated[ProductCookies, Cookie()]):
#     if cookies.session_id:
#         response = {"session_id": cookies.session_id}
#         if cookies.preferred_category:
#             response["message"] = f"Recommendations for {cookies.preferred_category} products"
#         else:
#             response["message"] = f"Default recommendations for session {cookies.session_id}"
#         if cookies.tracking_id:
#             response["tracking_id"] = cookies.tracking_id

#         return response
#     return {"message": "No session ID provided, showing default recommendations"}

# # # To test the above API run the below command in the terminal:
# # curl -H "Cookie: session_id=abc123; preferred_category=Electronics; tracking_id=xyz789" http://1
# # 27.0.0.1:8000/products/recommendations
# # {"session_id":"abc123","message":"Recommendations for Electronics products","tracking_id":"xyz789"}

# Using the extra parameters also as not forbidden for the extra parameters
# curl -H "Cookie: session_id=abc123; preferred_category=Electronics; extra-data=mydata; tracking_id=xyz789" http://127.0.0.1:8000/products/recommendations
# {"session_id":"abc123","message":"Recommendations for Electronics products","tracking_id":"xyz789"}

# ---------------------------------------------------------------

# # Forbidding Extra Cookies
# class ProductCookies(BaseModel):
#     model_config = {"extra": "forbid"} # this does not allow passing extra parameters from the terminal
#     session_id: str
#     preferred_category: str | None = None
#     tracking_id: str | None = None


# @app.get("/products/recommendations")
# async def get_recommendations(cookies: Annotated[ProductCookies, Cookie()]):
#     if cookies.session_id:
#         response = {"session_id": cookies.session_id}
#         if cookies.preferred_category:
#             response["message"] = f"Recommendations for {cookies.preferred_category} products"
#         else:
#             response["message"] = f"Default recommendations for session {cookies.session_id}"
#         if cookies.tracking_id:
#             response["tracking_id"] = cookies.tracking_id

#         return response
#     return {"message": "No session ID provided, showing default recommendations"}

# # # To test the above API run the below command in the terminal:
# # curl -H "Cookie: session_id=abc123; preferred_category=Electronics; extra-data=mydata; tracking_
# # id=xyz789" http://127.0.0.1:8000/products/recomme
# # ndations
# # {"detail":[{"type":"extra_forbidden","loc":["cookie","extra-data"],"msg":"Extra inputs are not permitted","input":"mydata"}]}

# ---------------------------------------------------------------

# Combining with Body Parameters
class ProductCookies(BaseModel):
    model_config = {"extra": "forbid"} # this does not allow passing extra parameters from the terminal
    session_id: str = Field(title="Session ID", description="User session identifier")
    preferred_category: str | None = Field(default=None, title="Preferred Category", description="User's preferred product category")


class PriceFilter(BaseModel):
    min_price: float = Field(ge=0, title="Minimum Price", description="Minimum price for recommendations")
    max_price: float | None = Field(default=None, title="Maximum Price", description="maximum price for recommendations")


@app.post("/products/recommendations")
async def get_recommendations(
    cookies: Annotated[ProductCookies, Cookie()],
    price_filter: Annotated[PriceFilter, Body(embed=True)]
    ):
    if cookies.session_id:
        response = {"session_id": cookies.session_id}
        if cookies.preferred_category:
            response["category"] = cookies.preferred_category

        response["price_range"] = {
            "min_price": price_filter.min_price,
            "max_price": price_filter.max_price
        }
        response["message"] = f"Recommendations for session {cookies.session_id} with price range {price_filter.min_price} to {price_filter.max_price or 'unlimited'}"
        return response
    return {"message": "No session ID provided, showing default recommendations"}

# # To test the above API in the terminal run the below command in the terminal:
# curl -X POST -H "Cookie: session_id=abc123; pre
# ferred_category=Electronics" -H "Content-Type:application/json" -d "{\"price_filter\":{\"min_price\":50.0,\"max_price\":1000.0}}" http://127.0.0.1:
# 8000/products/recommendations
# {"session_id":"abc123","category":"Electronics","price_range":{"min_price":50.0,"max_price":1000.0},"message":"Recommendations for session abc123 with price range 50.0 to 1000.0"}
