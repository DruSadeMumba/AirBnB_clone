#!/usr/bin/python3
"""The base class."""
from datetime import *
import uuid


class BaseModel:
    """A class that defines all common attributes/methods."""

    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """Initialize object attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today().strftime(self.DATE_FORMAT)
        self.updated_at = datetime.today().strftime(self.DATE_FORMAT)

    def __str__(self):
        """Print name id and dict"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with the current datetime"""
        self.created_at = datetime.today().strftime(self.DATE_FORMAT)

    def to_dict(self):
        """ Returns a dictionary rep of the instance"""
        dic = {key: value.isoformat() if isinstance(value, datetime) else value
               for key, value in self.__dict__.items()}
        dic["__class__"] = type(self).__name__
        return dic
