#!/usr/bin/python3
"""Implement the templated for the base class."""
import datetime
import uuid


class BaseModels:
    """Template for  all items for the HBNB Console."""
    def __init__(self, *args, **kwargs):
        """
        Instantiated the base models class.
            Args:
                *args: additional arguments provided to the program
                **kwargs: Additional key value to the program.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        pass
