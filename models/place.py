#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import Float, ForeignKey, Table, String, DateTime
import MySQLdb
from os import getenv
from models.city import City


"""
place_amenity = Table('place_amenity', Base.metadata, Column('place_id',
                      String(60), ForeignKey('places.id'), primary_key=True,
                      nullable=False),
                      Column('amenity_id', String(60), ForeignKey(amenities.id),
                      primary_key=True, nullable=False))"""


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    #amenity_ids = []

    """if getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship("Review", backref="place",
                               cascade='all, delete-orphan')
        amenities = relationship("Amenity",
                                 backref='places', viewonly=False)

    elif getenv("HBNB_TYPE_STORAGE") == 'file':
        @property
        def reviews(self):
            new = []
            for r in self.reviews:
                if r.place_id == self.id:
                    new.append(r)
            return new
    """
    """
        @property
        def amenities(self):
            new = []
            for obj in amenity_ids:
                if obj.id == self.id:
                    new.append(obj)
            return new
    """
    """
        @amenities.setter
        def amenities(self, obj):
            if type(obj) == 'Amenity':
                self.amenity_ids.append(obj.id)

    """
