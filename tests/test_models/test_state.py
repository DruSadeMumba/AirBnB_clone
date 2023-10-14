#!/usr/bin/python3
"""Unittest module for the State Class."""
import datetime
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test Cases for the State class."""
    new = State()
    attr_types = {
        'id': str,
        'created_at': datetime.datetime,
        'updated_at': datetime.datetime,
        'name': str
    }

    def setUp(self):
        """Set up tests"""
        super().setUp()

    def tearDown(self):
        """Tear down tests"""
        super().tearDown()

    def assertAttributes(self, instance):
        """attributes data types"""
        attr = ['id', 'created_at', 'updated_at', 'name']
        for attr_name in attr:
            self.assertTrue(hasattr(instance, attr_name))
            self.assertIsInstance(getattr(instance, attr_name), self.attr_types[attr_name])

    def test_instantiation(self):
        """Test instantiation of State class."""
        self.assertEqual(str(type(self.new)), "<class 'models.state.State'>")
        self.assertIsInstance(self.new, State)
        self.assertTrue(issubclass(type(self.new), BaseModel))
        self.assertAttributes(self.new)


if __name__ == '__main__':
    unittest.main()
