from app.schemas.Variant import Variant
from app.models.Variant import Variant as VariantModel
from fastapi.responses import JSONResponse
from datetime import datetime
from sqlmodel import Session

def createVariant(session: Session, variant: Variant, productId: int):
   v = VariantModel()
   v.sku = variant.sku
   v.sales_price = variant.sales_price
   v.product_id = productId
   v.type = variant.type
   v.config_attributes = variant.config_attributes
   v.purchase_price = variant.purchase_price
   v.created_at = datetime.now()
   v.updated_at = datetime.now()
   variantResponse = v.model_dump()
   
   try:
      session.add(v)
      session.commit()
   except:
      return JSONResponse(content={"error":f"an error ocurred creating the variant {v.sku}"},status_code=400)    
   else:
      variantResponse["id"] = v.id
      return variantResponse
   