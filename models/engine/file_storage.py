#!/usr/bin/python3
"""FileStorage Class"""
import json
import os
from models.base_model import BaseModel
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
