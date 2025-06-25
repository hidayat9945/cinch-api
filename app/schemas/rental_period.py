from pydantic import BaseModel

class RentalPeriodSchema(BaseModel):
    id: int
    duration_months: int

    class Config:
        orm_mode = True