#!/usr/bin/python3
"""The base class."""
from datetime import *
import uuid
import models


class BaseModel:
    """A class that defines all common attributes/methods."""
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Initialize object attributes"""
        if kwargs:
            for key, val in kwargs.items():
                if key in ("created_at", "updated_at"):
                    val = datetime.strptime(val, self.DATE_FORMAT)
                    setattr(self, key, val)
                else:
                    self.__dict__[key] = val
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """Print name id and dict"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary rep of the instance"""
        dic = {key: val.isoformat() if isinstance(val, datetime) else val
               for key, val in self.__dict__.items()}
        dic["__class__"] = type(self).__name__
        return dic

    @classmethod
    def all(cls):
        """retrieve all instances of a class."""
        class_instance = models.storage.find_instance(cls.__name__)
        return class_instance

    @classmethod
    def count(cls):
        """retrieve the number of instances of a class."""
        class_count = len(models.storage.find_instance(cls.__name__))
        return class_count

    @classmethod
    def show(cls, obj_id):
        """retrieve an instance based on its ID."""
        ist = models.storage.find_classname_id(cls.__name__, obj_id)
        return ist

    @classmethod
    def destroy(cls, obj_id):
        """destroy an instance based on his ID."""
        deleted_obj = models.storage.pop_classname_id(cls.__name__, obj_id)
        return deleted_obj

    @classmethod
    def update(cls, obj_id, *keys):
        """update the attrbutes of the class."""
        if len(keys) == 0:
            print("** attribute name missing **")
            return
        if len(keys) == 1 and type(keys[0]) == type(dict):
            keys = keys[0].items()
        else:
            keys = [keys[:2]]
        for arg in keys:
            models.storage.update_class(
                cls.__name__,
                obj_id,
                *arg
                )
