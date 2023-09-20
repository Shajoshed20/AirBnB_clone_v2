#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Representation of Amenity """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    
    if your_storage_type == 'db':
        place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)
    else:
        name = ""
