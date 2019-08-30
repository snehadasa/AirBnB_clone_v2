#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel, Base
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
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB"),
            pool_pre_ping=True))
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns list of objects
        Return:
            returns list of objects of type class
        """

        if cls:
            empty = self.__session.query(cls).all()
        else:
            empty = self.__session.query(State).all()
            empty += self.__session.query(City).all()
            empty += self.__session.query(User).all()
            empty += self.__session.query(Place).all()
            empty += self.__session.query(Review).all()
            empty += self.__session.query(Amenity).all()

        dic = {}
        for obj in empty:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            dic[key] = obj

        return dic

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
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                 expire_on_commit=False))
        self.__session = Session()

    def delete(self, obj=None):
        """delete obj from __session
           key = (arizona).id(id_created)
        """
        if obj:
            self.__session.delete(obj)

    def close(self):
        """call remove() method on the private session attribute(self.__session)
        """
        return self.__session.remove()
