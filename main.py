from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Products(BaseModel):
    name: str
    price: float
    stock: int

product_database = []

@app.post("/product")
def create_product(product: Products):

    product_database.append(product)

    return{
        "message" : "product added successfully"
    }

@app.get("/product")
def get_products():
    return product_database

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Products):

    product_database[product_id] = updated_product

    return{
        "message" : "product updated successfully",
        "updated product" : updated_product
    }

@app.delete("/product/{product_id}")
def delete_product(product_id: int):

    deleted_product = product_database.pop(product_id)

    return {
        "message" : "product deleted successfully",
        "deleted product" : deleted_product
    }
