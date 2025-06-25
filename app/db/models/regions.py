from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.timestamp_mixin import TimestampMixin

class Region(Base, TimestampMixin):
    __tablename__ = "regions"
    
    # columns
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    
    # relationships
    pricings = relationship("ProductPricing", back_populates="region", cascade="all, delete-orphan")
    