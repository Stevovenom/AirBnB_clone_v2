#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.amenity import Amenity

# Define the place_amenity table for the Many-to-Many relationship
place_amenity = Table('place_amenity', Base.metadata,
                      Column(
                          'place_id',
                          String(60),
                          ForeignKey('places.id'),
                          primary_key=True,
                          nullable=False
                          ),
                      Column(
                          'amenity_id',
                          String(60),
                          ForeignKey('amenities.id'),
                          primary_key=True,
                          nullable=False
                          )
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(
            String(60),
            ForeignKey('cities.id'),
            nullable=False
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db'
    else ''
    user_id = Column(
            String(60),
            ForeignKey('users.id'),
            nullable=False
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db'
    else ''
    name = Column(
            String(128),
            nullable=False
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db'
    else ''
    description = Column(
            String(1024)
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db'
    else ''
    number_rooms = Column(
            Integer,
            default=0,
            nullable=False
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db'
    else 0
    number_bathrooms = Column(
            Integer,
            default=0,
            nullable=False
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db'
    else 0
    max_guest = Column(
            Integer,
            default=0,
            nullable=False
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db'
    else 0
    price_by_night = Column(
            Integer,
            default=0,
            nullable=False
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db'
    else 0
    latitude = Column(
            Float
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db'
    else 0.0
    longitude = Column(
            Float
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db'
    else 0.0
    amenity_ids = []
    if os.getenv('HBNB_TYPE_STORAGE') != 'db'
    else None

    user = relationship(
            'User',
            back_populates='places'
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db'
    else None
    reviews = relationship(
            'Review',
            back_populates='place',
            cascade='all, delete-orphan'
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db'
    else None
    amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False
    )
    if os.getenv('HBNB_TYPE_STORAGE') == 'db'
    else None

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """Returns the list of Review instances"""
            from models import storage
            from models.review import Review
            return [review for review in storage.all(Review).values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """Returns the list of Amenity instances"""
            from models import storage
            from models.amenity import Amenity
            return [storage.all(Amenity).get(amenity_id)
                    for amenity_id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Setter for amenities that handles append method"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
