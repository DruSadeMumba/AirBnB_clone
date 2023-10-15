#!/usr/bin/python3
"""The base class."""
from datetime import datetime
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
        dic = self.__dict__.copy()
        dic["__class__"] = type(self).__name__
        dic["created_at"] = dic["created_at"].isoformat()
        dic["updated_at"] = dic["updated_at"].isoformat()
        return dic
