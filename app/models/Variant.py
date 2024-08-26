from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB

class Variant(SQLModel):
   id: Optional[int] = Field(default=None,primary_key=True)
   sku: str = Field(unique=True)
   sales_price: float
   product_id: Optional[int] = Field(default=None,foreign_key='product.id')
   purchase_price: float
   type: str
   created_at: datetime
   updated_at: datetime
   config_attributes: Optional[dict] = Field(default_factory=JSONB)