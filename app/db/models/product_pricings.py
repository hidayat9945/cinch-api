from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship
from ..base import Base
from ..timestamp_mixin import TimestampMixin

class ProductPricing(Base, TimestampMixin):
    __tablename__ = "product_pricings"
    
    # columns
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    rental_period_id = Column(Integer, ForeignKey("rental_periods.id"), nullable=False)
    region_id = Column(Integer, ForeignKey("regions.id"), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    
    # relationships
    product = relationship("Product", back_populates="pricings")
    rental_period = relationship("RentalPeriod", back_populates="pricings")
    region = relationship("Region", back_populates="pricings")
    
