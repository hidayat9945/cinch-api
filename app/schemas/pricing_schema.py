from pydantic import BaseModel
from app.schemas.region import RegionSchema
from app.schemas.rental_period import RentalPeriodSchema

class PricingSchema(BaseModel):
    id: int
    region: RegionSchema
    rental_period: RentalPeriodSchema
    price: float

    class Config:
        orm_mode = True