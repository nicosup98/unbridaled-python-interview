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
   created_at: datetime
   updated_at: datetime
   config_attributes: Optional[dict] 