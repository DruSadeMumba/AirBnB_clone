#!/usr/bin/python3
"""FileStorage Class"""
import json
import os
from models.base_model import BaseModel
from .custom_exceptions import *
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializing and deserializing of instances to and fro JSON file"""
    __file_path = "file.json"
    __objects = {}
    _FileStorage__file_path = __file_path
    _FileStorage__objects = __objects
    cls_list = (
        "BaseModel",
        "User", "City", "State", "Place",
        "Amenity", "Review"
    )

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in the obj with key"""
        FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dic = {key: val.to_dict()
                   for key, val in FileStorage.__objects.items()}
            json.dump(dic, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            dic = json.load(f)
        dic = {key: globals()[val["__class__"]](**val)
               for key, val in dic.items()}
        FileStorage.__objects = dic

    def pop_classname_id(self, class_list, input_1, input_2):
        """Deleted an instance of a class."""
        temp = FileStorage
        if input_1 not in temp.cls_list:
            raise ClassNameNotFoundError(input_1)

        k = input_1 + "." + input_2
        if k not in temp.__objects:
            raise InstanceIdNotFoundError(input_2, input_1)

        del temp.__objects[k]
        self.save()

    def find_classname_id(self, class_list, input_1, input_2):
        """Find given classname in the storage objects."""
        temp = FileStorage
        if input_1 not in temp.cls_list:
            raise ClassNameNotFoundError(input_1)

        k = input_1 + "." + input_2
        if k not in temp.__objects:
            raise InstanceIdNotFoundError(input_2, input_1)

        return temp.__objects[k]

    def find_instance(self, class_name=""):
        """Retrieve instance of the class_name."""
        if class_name and class_name not in FileStorage.cls_list:
            raise ClassNameNotFoundError(class_name)

        temp = list()
        for k, v in FileStorage.__objects.items():
            if k.startswith(class_name):
                temp.append(str(v))
        return temp
