from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..base import Base
from ..timestamp_mixin import TimestampMixin

class Attribute(Base, TimestampMixin):
    __tablename__ = "attributes"
    
    # columns
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    
    # relationships
    values = relationship("AttributeValue", back_populates="attribute", cascade="all, delete-orphan")