from pydantic import BaseModel
from sqlalchemy import Text
from typing import Optional

class Variant(BaseModel):
   id: Optional[int]
   sku: str
   sales_price: float
   product_id: Optional[int]
   purchase_price: float
   type: str
   config_attributes: Optional[dict] 