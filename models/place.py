#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ Airbnb place"""
    from models import env_storage
    __tablename__ = 'places'
    if env_storage == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", cascade="all, delete",
                               backref="state")
        amenities = []
    else:
        city_id = ''  # City.id
        user_id = ''  # User.id
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ Getter attribute that returns the list of Review
                instances with place_id equals to current Place.id
            """
            from models.review import Review
            list = []
            for i in models.storage.all(Review).values():
                if i.place_id == self.id:
                    list.append(i)
            return list

        @property
        def amenities(self):
            """ Getter attribute that returns the list of Amenity intances
                based on the attribute amenity_ids that contains all
                Amenity.id linked to the Place
            """
            from models.amenity import Amenity
            list = []
            for i in models.storage.all(Amenity).values():
                if i.place_id == self.id:
                    list.append(i)
            return list

        @amenities.setter
        def amenities(self, obj=None):
            """Add an Amenity id to the list Amenity_ids"""
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
