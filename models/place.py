#!/usr/bin/python3
"""The class of Place that inherits from BaseModel."""
from .base_model import BaseModel


class Place(BaseModel):
    """Representation of the Place class.

    Attributes:
        city_id (str): City's ID
        user_id (str): User's ID.
        name (str): Places's Name.
        description (str): Criteria for the Place.
        number_rooms (int): The No of rooms in the Place.
        number_bathrooms (int): The No of bathrooms.
        max_guest (int): The maximum guest to occupy place.
        price_by_night (int): The price per one night.
        latitude (float): The latitude coordinates.
        longitude (float): The longitude coordinates.
        amenity_ids (list): Amenity List.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
