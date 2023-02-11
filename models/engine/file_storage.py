#!/usr/bin/env python3

'''File Storage'''

import json
import models
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os.path as path
from models.base_model import BaseModel


class FileStorage:
    """serializing and deserializing instances
    to and from json files"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns dictionary: __objects"""
        return self.__objects

    def new(self, obj):
        """adds new object to dictionary"""
        if obj:
            obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[obj_key] = obj

    def save(self):
        """save directories to json"""
        my_dict = {}
        with open(self.__file_path, mode="w", encoding='UTF-8') as f:
            for key, value in self.__objects.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """convert existing json  dicts to instances"""
        try:
            if path.isfile(self.__file_path):
                with open(self.__file_path, mode="r", encoding='UTF-8') as f:
                    for key, value in json.load(f).items():
                        value = eval(value['__class__'])(**value)
                        self.__objects[key] = value
        except FileNotFoundError:
            pass
