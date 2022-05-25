#!/usr/bin/python3
""" DBstorage module """
from models.base_model import Base, BaseModel
from sqlalchemy import (create_engine)
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
           'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity,
           'Review': Review
          }


class DBStorage:
    """New engine to store the data in database"""
    __engine = None
    __session = None

    def __init__(self):
        """Environments variables defined"""
        mysql_user = getenv('HBNB_MYSQL_USER')
        mysql_pwd = getenv('HBNB_MYSQL_PWD')
        mysql_host = getenv('HBNB_MYSQL_HOST')
        mysql_db = getenv('HBNB_MYSQL_DB')
        mysql_env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(mysql_user, mysql_pwd,
                                             mysql_host, mysql_db),
                                      pool_pre_ping=True)
        if mysql_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a dictionary currently in the session"""
        dict = {}
        if cls is not None:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                dict[key] = obj.to_dict()
        else:
            for some in classes:
                objs = self.__session.query(classes[some]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dict[key] = obj.to_dict()
        return dict

    def new(self, obj):
        """Add the obj to the current session"""
        self.__session.add(obj)

    def save(self):
        """Commit the changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """If not None, delete the obj"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Public instance method that reload instances from db storage"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the session"""
        self.__session.close()
