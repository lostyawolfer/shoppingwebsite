from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import Function
import uvicorn

app = FastAPI()
db = Function()

class AddProduct(BaseModel):
    product_id: int
    name: str
    price: int
    description: str
    category: str

class UseProduct(BaseModel):
    product_id: int

@app.post("/add_product/")
def add_product(product: AddProduct):
    db.add_product(product.product_id, product.name, product.price, product.description, product.category)
    return {"message": "The product has been successfully added."}

@app.post("/get_product/")
def get_product(product: UseProduct):
    product_to_show = db.get_product(product.product_id)
    if product_to_show is None:
        raise HTTPException(status_code=404, detail='Product not found')
    formatted_document = {
        "product_id": product_to_show.product_id,
        "name": product_to_show.name,
        "price": product_to_show.price,
        "description": product_to_show.description,
        "category": product_to_show.category
    }
    return {"product": formatted_document}

@app.delete('/delete_product/')
def delete_product(product: UseProduct):
    product_to_delete = db.remove_product(product.product_id)
    if product_to_delete is None:
        raise HTTPException(status_code=404, detail='Product not found')

    return {"message": "Product successfully deleted"}



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)