from schemas.Product import ProductBody
from sqlmodel import Session
from fastapi.responses import JSONResponse
from models.Product import Product
from datetime import datetime
from .variant import createVariant

def createProduct(session: Session, product: ProductBody ):
   if product.name.lstrip() == "":
      
      return JSONResponse(content={"error":"name of product not defined"},status_code=500)
      
   p = Product()
   
   p.name = product.name
   p.is_producible = product.is_producible
   p.is_purchasable = product.is_purchasable
   p.additional_info = product.additional_info
   p.category_name = product.category_name
   p.batch_tracked = product.batch_tracked
   p.uom = product.uom
   p.type = product.type
   p.purchase_uom = product.purchase_uom
   p.purchase_uom_conversion_rate = product.purchase_uom_conversion_rate
   p.created_at = datetime.now()
   p.updated_at = datetime.now()
   
   #posible refactor: make this async
   for v in product.variants_id:
      resp = createVariant(session,v)
      
      if resp.status_code != 200:
         return resp
      
   
   
   
   return JSONResponse(content={"message":f"product {product.name} created"})