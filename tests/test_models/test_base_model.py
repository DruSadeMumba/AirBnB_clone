#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""
import unittest


def assert_raises_type_error(self, func, *args):
    """Error handler"""
    with self.assertRaises(TypeError) as e:
        func(args)
    err = f"{str(e.exception)}"
    self.assertEqual(str(e.exception), err)


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
        self.fail()

    def test_to_dict(self):
        """Test to_dic func"""
        self.fail()


if __name__ == '__main__':
    unittest.main()
