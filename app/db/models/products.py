from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from ..base import Base
from ..timestamp_mixin import TimestampMixin

class Product(Base, TimestampMixin):
    __tablename__ = "products"

    # columns
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    sku = Column(String(255), unique=True, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    # relationships
    category = relationship("Category", back_populates="product")
    attribute_values = relationship("AttributeValues", back_populates="product", cascade="all, delete-orphan")
    pricings = relationship("ProductPricing", back_populates="product", cascade="all, delete-orphan")
