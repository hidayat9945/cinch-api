from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.timestamp_mixin import TimestampMixin

class ProductAttributeValue(Base, TimestampMixin):
    __tablename__ = "product_attribute_values"
    
    # columns
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    attribute_value_id = Column(Integer, ForeignKey("attribute_values.id"), nullable=False)
    
    # relationships
    product = relationship("Product", back_populates="attribute_values")
    attribute_value = relationship("AttributeValue", back_populates="product_links")
    