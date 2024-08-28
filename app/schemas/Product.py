from pydantic import BaseModel
from .Variant import Variant
from typing import List, Optional
from decimal import Decimal
from datetime import datetime

class Product(BaseModel):
   id: Optional[int] = None
   name: str
   uom: str
   category_name: str
   is_producible: bool
   is_purchasable: bool
   type: str 
   purchase_uom: str
   purchase_uom_conversion_rate: float
   batch_tracked: bool
   additional_info: str
   
   
   
class ProductBody(Product):
   variants: List[Variant]
   

class ProductResponse(ProductBody):
   created_at: datetime
   updated_at: datetime

def validateProduct(product: ProductBody):
   return ProductBody.model_validate(product)