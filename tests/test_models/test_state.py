#!/usr/bin/python3
"""Unittest module for the State Class."""
import datetime
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    new = State()
    attr_types = {
        'id': str,
        'created_at': datetime.datetime,
        'updated_at': datetime.datetime,
        'name': str
    }

    def setUp(self) -> None:
        super().setUp()

    def tearDown(self) -> None:
        super().tearDown()

    def assertAttributes(self, instance):
        """attributes data types"""
        self.assertIsInstance(instance, State)
        self.assertTrue(issubclass(type(instance), BaseModel))

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
