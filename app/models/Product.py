from sqlmodel import SQLModel, Field
from typing import Optional
from sqlalchemy import Text
from datetime import datetime

class Product(SQLModel,table=True):
   id: Optional[int] = Field(default=None, primary_key=True)
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