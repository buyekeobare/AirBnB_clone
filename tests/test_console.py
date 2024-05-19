#!/usr/bin/python3
"""This script defines the unnitests for the console.py"""

import unittest
import os
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage

class Test_HBNBconsole(unittest.TestCase):
    """Unnittests for the HbnbConsole class"""

    def setUp(self):
        """Sets up tests envir for the console methods"""
        pass


class Test_HBNBprompt(unittest.TestCase):

    def test_prompt(self):
        """Unittests for the prompt and emptyline handling in the HBNBCommand class."""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        """Testing the prompt is correctly set to '(hbnb)'."""
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", mock_output.getvalue().strip())


class Test_HBNBcreate(unittest.TestCase):
    """Unittests for the create command in the HBNBCommand class"""

    def setUp(self):
        """Renames the file.json if it exists before running tests,
        and clears the FileStorage objects.."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    def tearDown(self):
        """Deletes 'file.json' if it exists, 
        and restores it from tmp after tests if it exists."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_with_missing_class(self):
        """Testing create command fails when no class name is provided."""
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(expected, mock_output.getvalue().strip())

    def test_create_with_invalid_class(self):
        """Testing create command with an invalid class name."""
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(expected, mock_output.getvalue().strip())

    def test_create_with_invalid_syntax(self):
        """Testing create command with invalid syntax."""
        expected = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(expected, mock_output.getvalue().strip())
        expected = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(expected, mock_output.getvalue().strip())

    def test_create_instances(self):
        """Testing the create command successfully creates instances 
    of different classes i.e BaseModel, User, State, City, Amenity, Place, Review,
    and checks that these instances are correctly added to the storage.
    """
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(mock_output.getvalue().strip()))
            testKey = "BaseModel.{}".format(mock_output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(mock_output.getvalue().strip()))
            testKey = "User.{}".format(mock_output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(mock_output.getvalue().strip()))
            testKey = "State.{}".format(mock_output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(mock_output.getvalue().strip()))
            testKey = "City.{}".format(mock_output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(mock_output.getvalue().strip()))
            testKey = "Amenity.{}".format(mock_output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(mock_output.getvalue().strip()))
            testKey = "Place.{}".format(mock_output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as mock_output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(mock_output.getvalue().strip()))
            testKey = "Review.{}".format(mock_output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())


if __name__ == "__main__":
    unittest.main()
