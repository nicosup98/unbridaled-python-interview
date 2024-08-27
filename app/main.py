from fastapi import FastAPI
from schemas.Product import ProductBody, Product
from db.engine import createEngine
from sqlmodel import Session
from controllers.products import createProduct

app = FastAPI()
db = None
@app.on_event("startup")
async def startup():
   db = createEngine()

@app.post("/v1/products/create",response_model=Product)
def handleCreateProduct(product: ProductBody):
   with Session(db) as session:
      resp = createProduct(session,product)
      
      if resp.status_code == 200:
         session.commit()
         
      session.close()
      return resp
         