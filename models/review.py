#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
import models


class Review(BaseModel, Base):
    """ Review class to store review information """
    from models import env_storage
    __tablename__ = 'reviews'
    if env_storage == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ''  # Place.id
        user_id = ''  # User.id
        text = ''
