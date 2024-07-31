#!/usr/bin/python3

# models/engine/db_storage.py

import os
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """This class creates the engine for a MySQL database storage system"""

    all_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate the engine and drop if test database"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            os.environ['HBNB_MYSQL_USER'],
            os.environ['HBNB_MYSQL_PWD'],
            os.environ['HBNB_MYSQL_HOST'],
            os.environ['HBNB_MYSQL_DB']), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects for current session based on class name"""
        obj_dict = {}

        if cls:
            cls_name = cls.__name__
            if cls_name in self.all_classes:
                cls = self.all_classes[cls_name]
                objects = self.__session.query(cls).all()
            else:
                return obj_dict  # or raise an exception if you prefer
        else:
            objects = self.__session.query(
                State, City, User, Amenity, Place, Review).all()

        for obj in objects:
            key = obj.__class__.__name__ + '.' + obj.id
            value = obj
            obj_dict[key] = value
        return obj_dict

    def new(self, obj):
        """Add object to current database session"""
        self.__session.add(obj)
        self.__session.flush()

    def save(self):
        """Commit changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create tables and current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call close on private session."""
        self.__session.remove()
