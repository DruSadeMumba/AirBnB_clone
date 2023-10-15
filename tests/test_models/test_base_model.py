#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


def assert_raises_type_error(self, func, *args):
    """Error handler"""
    with self.assertRaises(TypeError) as e:
        func(args)
    err = f"{str(e.exception)}"
    self.assertEqual(str(e.exception), err)


class TestBaseModel(unittest.TestCase):
    """Test cases for the FileStorage class"""
    base = BaseModel()
    vals = ["id", "created_at", "updated_at", "__class__"]

    def setUp(self):
        """Set up test methods."""
        super().setUp()
        FileStorage.__objects = {}

    def tearDown(self):
        """Tear down test methods."""
        super().tearDown()
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def id(self):
        """override Id"""
        return super().id()

    def test_instantiation(self):
        """Test instantiation of BaseModel class"""
        self.assertEqual(str(type(self.base)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(self.base, BaseModel)

    def test_save(self):
        """Test Save func"""
        assert_raises_type_error(self, self.base.save)
        assert_raises_type_error(self, self.base.save, "a")

    def test_to_dict(self):
        """Test to_dic func"""
        for obj in self.vals:
            with self.subTest(obj=obj):
                self.assertIn(obj, self.base.to_dict())

    def test_to_dict_err(self):
        assert_raises_type_error(self, self.base.to_dict)


if __name__ == '__main__':
    unittest.main()
