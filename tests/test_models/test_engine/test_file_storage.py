#!/usr/bin/python3
"""Unittest module for the FileStorage Class."""
import json
import os
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from models import FileStorage, storage


def assert_raises_type_error(self, func, *args):
    """Error handler"""
    with self.assertRaises(TypeError) as e:
        func(args)
    err = f"{str(e.exception)}"
    self.assertEqual(str(e.exception), err)


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""
    test_obj = [BaseModel(), Amenity(), City(), User(),
                Review(), State(), User()]

    def setUp(self):
        """Set up tests"""
        super().setUp()
        FileStorage.__objects = {}

    def tearDown(self):
        """Tear down tests"""
        super().tearDown()
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Test instantiation of FileStorage class"""
        self.assertEqual(str(type(FileStorage())), "<class 'models.engine.file_storage.FileStorage'>")
        self.assertIsInstance(FileStorage(), FileStorage)

    def assertAll(self, obj):
        """Test the all() function with a specific object."""
        key = f"{type(obj).__name__}.{obj.id}"
        storage.new(obj)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], obj)

    def assertAllObjs(self, objs):
        """Tests all() function with many objects for objs."""
        [storage.new(obj) for obj in objs]
        self.assertEqual(len(objs), len(storage.all()))
        for obj in objs:
            key = f"{type(obj).__name__}.{obj.id}"
            self.assertTrue(key in storage.all())
            self.assertEqual(storage.all()[key], obj)

    def test_all(self):
        """Test for all() function"""
        for obj in self.test_obj:
            with self.subTest(obj=obj):
                self.assertAll(obj)
                self.assertAllObjs(self.test_obj)

        assert_raises_type_error(self, storage.all)
        assert_raises_type_error(self, storage.all, "a")

    def assertNew(self, obj):
        """Test the new() function with a specific object."""
        storage.new(obj)
        key = f"{type(obj).__name__}.{obj.id}"
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], obj)

    def test_new(self):
        """Test for new() function"""
        for obj in self.test_obj:
            with self.subTest(obj=obj):
                self.assertNew(obj)

        assert_raises_type_error(self, FileStorage.new)
        assert_raises_type_error(self, FileStorage.new, "a")

    def assertSave(self, obj):
        """Test the save() function with a specific object."""
        self.tearDown()
        storage.new(obj)
        key = f"{type(obj).__name__}.{obj.id}"
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        d = {key: obj.to_dict()}
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_save(self):
        """Test for save() function"""
        for obj in self.test_obj:
            with self.subTest(obj=obj):
                self.assertSave(obj)

        assert_raises_type_error(self, storage.save)
        assert_raises_type_error(self, storage.save, "a")

    def assertReload(self, obj):
        """Test the reload() function with a specific object."""
        self.tearDown()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        storage.new(obj)
        key = f"{type(obj).__name__}.{obj.id}"
        storage.save()
        obj.name = "Cat"
        storage.reload()
        self.assertNotEqual(obj.to_dict(), storage.all()[key].to_dict())

    def test_reload(self):
        """Test for reload() function"""
        for obj in self.test_obj:
            with self.subTest(obj=obj):
                self.assertReload(obj)

        assert_raises_type_error(self, storage.reload)
        assert_raises_type_error(self, storage.reload, "a")


if __name__ == '__main__':
    unittest.main()
