from schemas.Variant import Variant
from models.Variant import Variant as VariantModel
from fastapi.responses import JSONResponse
from datetime import datetime
from sqlmodel import Session

def createVariant(session: Session, variant: Variant):
   if variant.sales_price is None:
      return JSONResponse(content={"error":"sales_price in variant not defined"},status_code=400)
   
   if variant.product_id is None:
      return JSONResponse(content={"error":"product_id in variant not defined"},status_code=400)
   
   v = VariantModel()
   v.sku = variant.sku
   v.sales_price = variant.sales_price
   v.product_id = variant.product_id
   v.type = variant.type
   v.config_attributes = variant.config_attributes
   v.purchase_price = variant.purchase_price
   v.created_at = datetime.now()
   v.updated_at = datetime.now()
   
   session.add(v)
   
   return JSONResponse(content={"message":"variant created"})
   