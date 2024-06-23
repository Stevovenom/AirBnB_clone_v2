#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel):
    """ State class """
    __tablename__ = 'state'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('city', backref='state', cascade='all, delete, delete-orphan')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initialize state"""
        super().__init__(*args, **kwargs)
