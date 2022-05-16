#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity to have"""
    from models import env_storage
    __tablename__ = 'amenities'
    if env_storage == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       viewonly=False)
    else:
        name = ''
