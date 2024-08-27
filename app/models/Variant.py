from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from decimal import Decimal

class Variant(SQLModel, table=True):
   id: Optional[int] = Field(default=None,primary_key=True)
   sku: str = Field(unique=True)
   sales_price: Optional[Decimal] = Field(default=None,decimal_places=2)
   product_id: Optional[int] = Field(default=None,foreign_key='product.id')
   purchase_price: Optional[Decimal] = Field(default=None, decimal_places=2)
   type: str
   created_at: datetime
   updated_at: datetime
   config_attributes: Optional[dict] = Field(default_factory=JSONB)