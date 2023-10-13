#!/usr/bin/python3
"""Unittest module for the City Class."""
import datetime
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    new = City()
    attr_types = {
        'id': str,
        'created_at': datetime.datetime,
        'updated_at': datetime.datetime,
        'state_id': str,
        'name': str
    }

    def setUp(self):
        """Sets up test methods."""
        super().setUp()

    def tearDown(self):
        """Tears down test methods."""
        super().tearDown()

    def assertAttributes(self, instance):
        """attributes data types"""
        self.assertIsInstance(instance, City)
        self.assertTrue(issubclass(type(instance), BaseModel))

        attr = ['id', 'created_at', 'updated_at', 'state_id', 'name']
        for attr_name in attr:
            self.assertTrue(hasattr(instance, attr_name))
            self.assertIsInstance(getattr(instance, attr_name), self.attr_types[attr_name])

    def test_instantiation(self):
        """Test instantiation of City class."""
        self.assertEqual(str(type(self.new)), "<class 'models.city.City'>")
        self.assertIsInstance(self.new, City)
        self.assertTrue(issubclass(type(self.new), BaseModel))
        self.assertAttributes(self.new)


if __name__ == '__main__':
    unittest.main()
