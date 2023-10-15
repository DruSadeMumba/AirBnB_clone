#!/usr/bin/python3
"""Unittest for the command interpreter(Console)."""


import unittest
import os
import sys
from unittest.mock import patch
from models import storage
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from io import StringIO


class TestConsolePrompt(unittest.TestCase):
    """Implement unittest for prompt."""

    def test_prompt(self):
        self.assertEqual("(hbnb)> ", HBNBCommand.prompt)

    def test_emptyline(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())


class TestConsoleHelp(unittest.TestCase):
    """Implement unittest for help."""

    def test_h_quit(self):
        h = "Exit the console."
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, f.getvalue().strip())

    def test_h_create(self):
        h = "Creating a new instance of BaseModel,save it, and print the id."
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(h, f.getvalue().strip())

    def test_h_EOF(self):
        h = "Exiting the console when reach EOF."
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(h, f.getvalue().strip())

    def test_h_all(self):
        h = "Display all instances provided with classname or not."
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(h, f.getvalue().strip())


class TestConsoleExiting(unittest.TestCase):
    """Unittest test for exiting the command interpreter."""

    def test_e_exit(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_e_EOF(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestConsoleCreate(unittest.TestCase):
    """Unittest test for testing the creation of the classes."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "new")
        except IOError:
            pass
        FileStorage.__objects.clear()

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("new", "file.json")
        except IOError:
            pass

    def test_create_no_classname(self):
        message = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(message, f.getvalue().strip())

    def test_create_unlisted_class(self):
        message = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create basemodel"))
            self.assertEqual(message, f.getvalue().strip())

    def test_create_class_not_found(self):
        message = "*** Not found: User.create()"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("User.create()"))
            self.assertEqual(correct, f.getvalue().strip())

    def test_create_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            captured_f = f.getvalue().strip()
            self.assertLess(0, len(captured_f))
            testKey = f"BaseModel.{captured_f}"
            self.assertIn(testKey, storage.all().keys())


class TestConsoleShow(unittest.TestCase):
    """Unittest test for testing the show of the classes."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "new")
        except IOError:
            pass
        FileStorage.__objects.clear()

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("new", "file.json")
        except IOError:
            pass

    def test_show_no_classname(self):
        message = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(message, f.getvalue().strip())

    def test_show_unlisted_class(self):
        message = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show basemodel"))
            self.assertEqual(message, f.getvalue().strip())

    def test_show_class_no_id(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(message, f.getvalue().strip())

    def test_show_invalid_syntax(self):
        message = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User()"))
            self.assertEqual(message, f.getvalue().strip())

    def test_show_class_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            class_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            ist = storage.all()["BaseModel.{}".format(class_id)]
            arg = "BaseModel.show({})".format(class_id)
            self.assertFalse(HBNBCommand().onecmd(arg))
            self.assertEqual(ist.__str__(), f.getvalue().strip())


class TestConsoleDestroy(unittest.TestCase):
    """Unittest test for testing the destroy of the classes."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "new")
        except IOError:
            pass
        FileStorage.__objects.clear()

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("new", "file.json")
        except IOError:
            pass

    def test_destroy_no_classname(self):
        message = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(message, f.getvalue().strip())

    def test_destroy_unlisted_class(self):
        message = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy basemodel"))
            self.assertEqual(message, f.getvalue().strip())

    def test_destroy_class_no_id(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(message, f.getvalue().strip())

    def test_destroy_invalid_syntax(self):
        message = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User()"))
            self.assertEqual(message, f.getvalue().strip())

    def test_destroy_class_no_found(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User 3"))
            self.assertEqual(message, f.getvalue().strip())

    def test_destroy_class_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            class_id = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["BaseModel.{}".format(class_id)]
            arg = "destroy BaseModel {}".format(class_id)
            self.assertFalse(HBNBCommand().onecmd(arg))
            self.assertNotIn(obj, storage.all())


class TestConsoleAll(unittest.TestCase):
    """Unittest test for testing the all of the classes."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "new")
        except IOError:
            pass
        FileStorage.__objects.clear()

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("new", "file.json")
        except IOError:
            pass

    def test_all_unlisted_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all basemodel"))
            self.assertEqual(correct, f.getvalue().strip())

    def test_all_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", f.getvalue().strip())

    def test_all_one_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", f.getvalue().strip())


class TestConsoleAll(unittest.TestCase):
    """Unittest test for testing the all of the classes."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "new")
        except IOError:
            pass
        FileStorage.__objects.clear()

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("new", "file.json")
        except IOError:
            pass

    def test_update_no_classname(self):
        message = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(message, f.getvalue().strip())

    def test_update_unlisted_class(self):
        message = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update basemodel"))
            self.assertEqual(message, f.getvalue().strip())

    def test_update_class_no_id(self):
        message = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(message, f.getvalue().strip())

    def test_update_invalid_syntax(self):
        message = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User()"))
            self.assertEqual(message, f.getvalue().strip())

    def test_update_class_no_found(self):
        message = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("update User 3"))
            self.assertEqual(message, f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
