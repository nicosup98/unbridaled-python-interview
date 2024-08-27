from sqlmodel import SQLModel, Field
from typing import Optional
from sqlalchemy import Text
from datetime import datetime
from decimal import Decimal

class Product(SQLModel,table=True):
   id: Optional[int] = Field(default=None, primary_key=True)
   name: str
   uom: str
   category_name: str
   is_producible: bool
   is_purchasable: bool
   type: str 
   purchase_uom: Optional[Decimal] = Field(default=None,decimal_places=2)
   purchase_uom_conversion_rate: Decimal = Field(default=1,max_digits=4,decimal_places=3)
   batch_tracked: bool
   additional_info: Text
   created_at: datetime
   updated_at: datetime