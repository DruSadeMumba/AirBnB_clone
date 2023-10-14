#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""
import unittest


class TestBaseModel(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up test methods."""
        super().setUp()

    def tearDown(self):
        """Tear down test methods."""
        super().tearDown()

    def id(self):
        """override Id"""
        return super().id()

    def test_save(self):
        """Test Save func"""
        pass

    def test_to_dict(self):
        """Test to_dic func"""
        pass


if __name__ == '__main__':
    unittest.main()
