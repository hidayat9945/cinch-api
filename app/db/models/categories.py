from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.timestamp_mixin import TimestampMixin

class Category(Base, TimestampMixin):
    __tablename__ = "categories"
    
    # columns
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    
    # relationships
    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")