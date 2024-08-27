from pydantic import BaseModel
from .Variant import Variant
from typing import List
from decimal import Decimal
class Product(BaseModel):
   id: Optional[int]
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
   
   
   
class ProductBody(Product):
   variants_id: List[Variant]