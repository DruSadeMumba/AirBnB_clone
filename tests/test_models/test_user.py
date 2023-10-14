#!/usr/bin/python3
"""Unittest module for the User Class."""
import datetime
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test Cases for the User class."""
    new = User()
    attr_types = {
        'id': str,
        'created_at': datetime.datetime,
        'updated_at': datetime.datetime,
        'email': str,
        'password': str,
        'first_name': str,
        'last_name': str
    }

    def setUp(self):
        """Set up tests"""
        super().setUp()

    def tearDown(self):
        """Tear down tests"""
        super().tearDown()

    def assertAttributes(self, instance):
        """attributes data types"""
        attr = ['id', 'created_at', 'updated_at', 'email', 'password', 'first_name', 'last_name']
        for attr_name in attr:
            self.assertTrue(hasattr(instance, attr_name))
            self.assertIsInstance(getattr(instance, attr_name), self.attr_types[attr_name])

    def test_instantiation(self):
        """Test instantiation of User class."""
        self.assertEqual(str(type(self.new)), "<class 'models.user.User'>")
        self.assertIsInstance(self.new, User)
        self.assertTrue(issubclass(type(self.new), BaseModel))
        self.assertAttributes(self.new)


if __name__ == '__main__':
    unittest.main()
