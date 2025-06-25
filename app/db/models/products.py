from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.timestamp_mixin import TimestampMixin
from app.db.models.categories import Category
from app.db.models.attribute_values import AttributeValue
from app.db.models.product_pricings import ProductPricing

class Product(Base, TimestampMixin):
    __tablename__ = "products"

    # columns
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    sku = Column(String(255), unique=True, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    # relationships
    category = relationship("Category", back_populates="products")
    attribute_values = relationship("ProductAttributeValue", back_populates="product", cascade="all, delete-orphan")
    pricings = relationship("ProductPricing", back_populates="product", cascade="all, delete-orphan")
