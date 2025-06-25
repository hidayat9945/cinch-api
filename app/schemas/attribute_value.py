from pydantic import BaseModel
from app.schemas.attribute import AttributeSchema

class AttributeValueSchema(BaseModel):
    id: int
    value: str
    attribute: AttributeSchema

    class Config:
        orm_mode = True