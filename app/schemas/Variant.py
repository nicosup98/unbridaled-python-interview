from pydantic import BaseModel
from sqlalchemy import Text
from typing import Optional, List
from decimal import Decimal

class Variant(BaseModel):
   id: Optional[int] = None
   sku: str
   sales_price: Decimal
   product_id: Optional[int] = None
   purchase_price: Decimal
   type: str
   config_attributes: Optional[List[dict]] 
   
   
def validateVariant(variant: Variant):
   return Variant.model_validate(variant)