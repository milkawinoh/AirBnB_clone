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
    attributes:
        __file_path: string - path to the JSON file.
        __objects: dictionary - empty but will store
            all objects by <class name>.id.
    """

    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)

        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dic_data = {}
        for key, obj in self.__objects.items():
            dic_data[key] = obj.to_dict()
            with open(self.__file_path, "w", encoding="utf-8") as json_file:
                json.dump(dic_data, json_file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        ; otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data_dic = json.load(file)
                for key, value in data_dic.items():
                    class_name, object_id = key.split(".")
                    if class_name in self.classes:
                        cls = self.classes[class_name]
                        value = cls(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
