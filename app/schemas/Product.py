from pydantic import BaseModel
from .Variant import Variant
from typing import List
class Product(BaseModel):
   name: str
   uom: str
   category_name: str
   is_producible: bool
   is_purchasable: bool
   type: str 
   purchase_uom: float
   purchase_uom_conversion_rate: float
   batch_tracked: bool
   additional_info: Text
   created_at: datetime
   updated_at: datetime
   
class ProductResponse(Product):
   id: int
   variant: List[Variant]
   
class ProductBody(Product):
   variant_id: int