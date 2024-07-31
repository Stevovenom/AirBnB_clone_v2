#!/usr/bin/python3
"""This module defines a class User"""
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
#from models.place import Place  # Ensure correct import
#from models.review import Review  # Ensure correct import

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    password = Column(String(128), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    first_name = Column(String(128)) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    last_name = Column(String(128)) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship('Place', back_populates='user', cascade='all, delete, delete-orphan') if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
