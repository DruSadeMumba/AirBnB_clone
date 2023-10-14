#!/usr/bin/python3
"""Unittest module for the Review Class."""
import datetime
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test Cases for the Review class."""
    new = Review()
    attr_types = {
        'id': str,
        'created_at': datetime.datetime,
        'updated_at': datetime.datetime,
        'place_id': str,
        'user_id': str,
        'text': str
    }

    def setUp(self):
        """Set up tests"""
        super().setUp()

    def tearDown(self):
        """Tear down tests"""
        super().tearDown()

    def assertAttributes(self, instance):
        """attributes data types"""
        attr = ['id', 'created_at', 'updated_at', 'place_id', 'user_id', 'text']
        for attr_name in attr:
            self.assertTrue(hasattr(instance, attr_name))
            self.assertIsInstance(getattr(instance, attr_name), self.attr_types[attr_name])

    def test_instantiation(self):
        """Test instantiation of Review class."""
        self.assertEqual(str(type(self.new)), "<class 'models.review.Review'>")
        self.assertIsInstance(self.new, Review)
        self.assertTrue(issubclass(type(self.new), BaseModel))
        self.assertAttributes(self.new)


if __name__ == '__main__':
    unittest.main()
