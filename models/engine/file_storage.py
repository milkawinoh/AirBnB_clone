#!/usr/bin/pythpn3
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
"""
module that that serializes instances to a
JSON file and deserializes JSON file to instances:
"""


class FileStorage:
    """
    This class manages the serialization and deserialization of all instances to and from JSON.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store all objects, with the keys as "<class name>.id".
    """

    def __init__(self):
        """
        Initializes a new FileStorage instance.
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value['__class__']
                    obj = eval(class_name + "(**value)")
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
