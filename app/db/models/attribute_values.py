from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..base import Base
from ..timestamp_mixin import TimestampMixin

class AttributeValue(Base, TimestampMixin):
    __tablename__ = "attribute_values"
    
    # columns
    id = Column(Integer, primary_key=True)
    value = Column(String(255), nullable=False)
    attribute_id = Column(Integer, ForeignKey("attributes.id"), nullable=False)
    
    # relationships
    attribute = relationship("Attribute", back_populates="values")
    products = relationship("ProductAttributeValue", back_populates="attribute_value", cascade="all, delete-orphan")