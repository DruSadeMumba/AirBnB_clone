#!/usr/bin/python3
"""FileStorage Class"""


class FileStorage:
    """A class that serializes and deserializes instances to and fro JSON file"""
    __file_path = "file_storage.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in the obj with key"""
        pass

    def save(self):
        """serializes __objects to the JSON file"""
        pass

    def reload(self):
        """Deserializes the JSON file to __objects"""
        pass
