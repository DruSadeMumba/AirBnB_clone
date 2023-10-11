#!/usr/bin/python3
"""The class of Amenity that inherits from BaseModel class."""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Representation of the Amenity class.
    Attributes:
        name(str): The class of Amenity
    """
    name = ""
