#!/usr/bin/python3
""" Place Module for HBNB project """
import os  # Add this line to import the os module

from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    name = Column(String(128), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    description = Column(String(1024)) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    number_rooms = Column(Integer, default=0, nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    number_bathrooms = Column(Integer, default=0, nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    max_guest = Column(Integer, default=0, nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    price_by_night = Column(Integer, default=0, nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    latitude = Column(Float) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0
    longitude = Column(Float) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0
    amenity_ids = [] if os.getenv('HBNB_TYPE_STORAGE') != 'db' else None
    user = relationship('User', back_populates='places') if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
