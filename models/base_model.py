#!/usr/bin/python3
"""The base class."""
from datetime import *
import uuid


class BaseModel:
    """A class that defines all common attributes/methods."""
    def __init__(self, *args, **kwargs):
        """Initialize object attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """Print name id and dict"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates updated_at with the current datetime"""
        self.created_at = datetime.today()
        pass

    def to_dict(self):
        pass
