#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ == 'states'

    if getenv(HBNB_TYPE_STORAGE) = "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state')
    else:
        name = ""

        @property
        def cities(self):
            for value in models.storage.all(City).values():
                if value.state_id == self.id:
                    return value
