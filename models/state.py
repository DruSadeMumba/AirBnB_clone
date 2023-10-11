#!/usr/bin/python3
"""The State class that inherits from the base model."""
from .base_model import BaseModel


class State(BaseModel):
    """
    Representation of the state class.
    Attributes:
        name (str): States' name
    """
    name = ""
