from pydantic import BaseModel
from .attribute import AttributeSchema

class AttributeValueSchema(BaseModel):
    id: int
    value: str
    attribute: AttributeSchema

    class Config:
        orm_mode = True