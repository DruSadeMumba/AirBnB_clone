#!/usr/bin/python3
"""Review Class that inherits from the BaseModel."""
from .base_model import BaseModel


class Review(BaseModel):
    """Representation of a class of review.
    Attributes:
        place_id (str): Place ID
        user_id (str): User ID.
        text (str): Review Text.
    """
    place_id = ""
    user_id = ""
    text = ""
