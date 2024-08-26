from schemas.Product import ProductBody
from sqlmodel import Session
from fastapi.responses import JSONResponse

def createProduct(session: Session, product: ProductBody ):
   if product['name'] is None:
      session.close()
      return JSONResponse(content={"error":"name of product not defined"},status_code=500)
      
   session.add(product)