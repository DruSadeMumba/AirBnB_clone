#!/usr/bin/python3
"""Unittest module for the Amenity Class."""
import datetime
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test Cases for the Amenity class."""
    new = Amenity()
    attr_types = {
        'id': str,
        'created_at': datetime.datetime,
        'updated_at': datetime.datetime,
        'name': str
    }

    def setUp(self):
        """Set up test methods."""
        super().setUp()

    def tearDown(self):
        """Tear down test methods."""
        super().tearDown()

    def assertAttributes(self, instance):
        """Attributes data types"""
        attr = ['id', 'created_at', 'updated_at', 'name']
        for attr_name in attr:
            self.assertTrue(hasattr(instance, attr_name))
            self.assertIsInstance(getattr(instance, attr_name),
                                  self.attr_types[attr_name])

    def test_instantiation(self):
        """Test instantiation of Amenity class."""
        self.assertEqual(str(type(self.new)),
                         "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(self.new, Amenity)
        self.assertTrue(issubclass(type(self.new), BaseModel))
        self.assertAttributes(self.new)


if __name__ == "__main__":
    unittest.main()
