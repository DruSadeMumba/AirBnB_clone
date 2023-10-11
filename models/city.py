#!/usr/bin/python3
"""City class that inherits from the BaseModel Class."""
from .base_model import BaseModel


class City(BaseModel):
    """Define the City class.

    Attributes:
        state_id (str): the ID of the state
        name (str): the city name
    """

    state_id = ""
    name = ""
