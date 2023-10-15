#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""
import os
import unittest
import uuid
from datetime import datetime

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
        """Tests the public instance method to_dict()."""
        self.base.name = "Cat"
        self.base.age = 3
        dic = self.base.to_dict()
        self.assertEqual(dic["id"], self.base.id)
        self.assertEqual(dic["__class__"], type(self.base).__name__)
        self.assertEqual(dic["created_at"], self.base.created_at.isoformat())
        self.assertEqual(dic["updated_at"], self.base.updated_at.isoformat())
        self.assertEqual(dic["name"], self.base.name)
        self.assertEqual(dic["age"], self.base.age)

    def test_to_dict_args(self):
        """Tests to_dict() with no arguments."""
        self.tearDown()
        assert_raises_type_error(self, self.base.to_dict())
        assert_raises_type_error(self, self.base.to_dict, "a")

    def test_to_dict_instantiation(self):
        """Tests instantiation with **kwargs."""
        my_model = BaseModel()
        my_model.name = "Abc"
        my_model.my_number = 5
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    def test_instantiation_dict(self):
        """Tests instantiation with **kwargs from custom dict."""
        dic = {"__class__": "BaseModel",
             "updated_at":
             datetime(2000, 11, 3, 20, 59, 59, 123456).isoformat(),
             "created_at": datetime.now().isoformat(),
             "id": uuid.uuid4(),
             "var": "blah",
             "int": 4,
             "float": 3.14}
        obj = BaseModel(**dic)
        self.assertEqual(obj.to_dict(), dic)


if __name__ == '__main__':
    unittest.main()
