from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.timestamp_mixin import TimestampMixin
from app.db.models.attributes import Attribute
from app.db.models.product_attribute_values import ProductAttributeValue

class AttributeValue(Base, TimestampMixin):
    __tablename__ = "attribute_values"
    
    # columns
    id = Column(Integer, primary_key=True)
    value = Column(String(255), nullable=False)
    attribute_id = Column(Integer, ForeignKey("attributes.id"), nullable=False)
    
    # relationships
    attribute = relationship("Attribute", back_populates="values")
    product_links = relationship("ProductAttributeValue", back_populates="attribute_value", cascade="all, delete-orphan")