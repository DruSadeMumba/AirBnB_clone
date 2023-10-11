#!/usr/bin/python3
"""User class"""
from models import BaseModel


class User(BaseModel):
    """Class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
