#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = 'states'

    name = Column(String(128),
                  nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete-orphan")

    else:
        @property
        def cities(self):
            empty = []
            for value in models.storage.all('City').items():
                if value.state_id == self.id:
                    empty.append(value)
            return(empty)

"""    else:
        @property
        def cities(self):
            empty = []
            for n, value in models.storage.all(City).items():
                if value.state_id == self.id:
                    empty.append(value)
            return(empty)"""
