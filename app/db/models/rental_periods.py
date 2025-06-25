from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from ..base import Base
from ..timestamp_mixin import TimestampMixin

class RentalPeriod(Base, TimestampMixin):
    __tablename__ = "rental_periods"
    
    # columns
    id = Column(Integer, primary_key=True)
    duration_months = Column(Integer, nullable=False)
    
    # relationships
    pricings = relationship("ProductPricing", back_populates="rental_period", cascade="all, delete-orphan")