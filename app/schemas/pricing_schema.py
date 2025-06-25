from pydantic import BaseModel
from .region import RegionSchema
from .rental_period import RentalPeriodSchema

class PricingSchema(BaseModel):
    id: int
    region: RegionSchema
    rental_period: RentalPeriodSchema
    price: float

    class Config:
        orm_mode = True