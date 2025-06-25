from typing import List, Optional
from pydantic import BaseModel
from .category import CategorySchema
from .attribute_value import AttributeValueSchema
from .pricing_schema import PricingSchema

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
