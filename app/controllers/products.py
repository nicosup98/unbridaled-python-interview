from sqlmodel import Session
from fastapi.responses import JSONResponse
from app.models.Product import Product
from datetime import datetime
from .variant import createVariant
from app.schemas.Product import validateProduct, ProductBody

def createProduct(session: Session, product: ProductBody ):
   
   try:
      validateProduct(product)
   except ValidationError:
      return JSONResponse(content={"error":"an error occurred during product validation"},status_code=400)
   else:
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

      session.add(p)
      session.commit()
      variants = []
      #posible refactor: make this async
      for v in product.variants:
         resp = createVariant(session,v,p.id)
         
         if isinstance(resp,JSONResponse):
            return resp
         variants.append(resp.model_dump())
      
      productResponse = p.model_dump()
      productResponse["variants"] = variants
      productResponse["created_at"] = p.created_at
      productResponse["updated_at"] = p.updated_at
      return productResponse