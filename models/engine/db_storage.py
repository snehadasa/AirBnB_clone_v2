#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __engine = None
    __session = None

    def __init__(self):
        """creating an engine and linking to databases
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            (getenv("HBNB_MYSQL_USER"),
             getenv("HBNB_MYSQL_PWD"),
             getenv("HBNB_MYSQL_HOST"),
             getenv("HBNB_MYSQL_DB"), pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
             Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns list of objects
        Return:
            returns list of objects of type class
        """
        if cls:
            dic={}
            for key, obj in self.__objects.items():
                if isinstance(key, cls):
                    dic[obj]=key
            return dic
        else:
            return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
            self.__session.add(obj)

    def save(self):
        """serialize the file path to JSON file path
        """
        self.__session.commit()

    def reload(self):
        """serialize the file path to JSON file path
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def delete(self, obj=None):
        """delete obj from __session
           key = (arizona).id(id_created)
        """
        if obj is not None:
            self.__session.delete(obj)
