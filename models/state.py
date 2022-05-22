#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    from models import env_storage
    __tablename__ = 'states'
    if env_storage == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """getter attribute cities that returns the list of City
            instances with state_id equals to the current State.id"""
            id_list = []
            for i in models.storage.all(City).values():
                if i.state_id == self.id:
                    id_list.append(i)
            return id_list
