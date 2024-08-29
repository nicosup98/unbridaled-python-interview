from fastapi import FastAPI
from app.schemas.Product import ProductBody, Product, ProductResponse
from app.db.engine import createEngine
from sqlmodel import Session
from app.controllers.products import createProduct
from fastapi.responses import JSONResponse
from typing import Union


app = FastAPI()

@app.post("/v1/products/create")
async def handleCreateProduct(product: ProductBody):
   db = createEngine()
   with Session(db) as session:
      return createProduct(session,product)
         