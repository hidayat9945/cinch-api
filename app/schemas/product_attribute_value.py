from pydantic import BaseModel
from app.schemas.attribute_value import AttributeValueSchema

class ProductAttributeValueSchema(BaseModel):
    attribute_value: AttributeValueSchema
    
    class Config:
        orm_mode = True