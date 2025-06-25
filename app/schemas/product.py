from typing import List, Optional
from pydantic import BaseModel
from app.schemas.category import CategorySchema
from app.schemas.attribute_value import AttributeValueSchema
from app.schemas.pricing_schema import PricingSchema

class ProductSchema(BaseModel):
    id: int
    name: str
    description: Optional[str]
    sku: str
    category: Optional[CategorySchema]
    attribute_values: List[AttributeValueSchema]
    pricings: List[PricingSchema]

    class Config:
        orm_mode = True
