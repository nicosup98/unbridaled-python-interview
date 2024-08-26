from fastapi import FastAPI
from schemas.Product import ProductBody, ProductResponse
app = FastAPI()

@app.post("/v1/products/create",response_model=ProductResponse)
def handleCreateProduct(product: ProductBody):
   return "hello"