#!/usr/bin/python3
"""This script the defines unittests for models/user.py."""

import unittest
import models
import os
from models.user import User
from datetime import datetime
from time import sleep


class Test_User_instantiation(unittest.TestCase):
    """Unittests for testing the creation of the State class instances."""

    def test_instantiates_no_args(self):
        """Testing a Place instance can be instantiated with no arguments."""
        self.assertEqual(User, type(User()))

    def test_new_instance_in_objects(self):
        """Testing a new Place instance is stored in the objects dictionary."""
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Testing the id attribute is a public string."""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """Testing the created_at attribute is a public datetime."""
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        """Testing the updated_at attribute is a public datetime."""
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        """Testing the email attribute is a public string."""
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        """Testing the passwword attribute is a public string."""
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        """Testing the first_name attribute is a public string."""
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        """Testing the last_name attribute is a public string."""
        self.assertEqual(str, type(User.last_name))

    def test_unique_ids_for_two_users(self):
        """Testing two places instances have unique ids."""
        usr1 = User()
        usr2 = User()
        self.assertNotEqual(usr1.id, usr2.id)

    def test_different_created_at_for_two_users(self):
        """Testing two places instances have different created_at values."""
        usr1 = User()
        sleep(0.05)
        usr2 = User()
        self.assertLess(usr1.created_at, usr2.created_at)

    def test_different_updated_at_for_two_users(self):
        """Testing two places instances have different updated_at values."""
        usr1 = User()
        sleep(0.05)
        usr2 = User()
        self.assertLess(usr1.updated_at, usr2.updated_at)

    def test_str_representation(self):
        """Testing the string representation of an class instance."""
        dtm = datetime.today()
        dtm_repr = repr(dtm)
        usr = User()
        usr.id = "456789"
        usr.created_at = usr.updated_at = dtm
        usrstr = usr.__str__()
        self.assertIn("[User] (456789)", usrstr)
        self.assertIn("'id': '456789'", usrstr)
        self.assertIn("'created_at': " + dtm_repr, usrstr)
        self.assertIn("'updated_at': " + dtm_repr, usrstr)

    def test_args_not_used(self):
        """Testing arguments not used do not affect instantiation."""
        usr = User(None)
        self.assertNotIn(None, usr.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Testing instantiation with keyword arguments."""
        dtm = datetime.today()
        dtm_format = dtm.isoformat()
        usr = User(id="456", created_at=dtm_format, updated_at=dtm_format)
        self.assertEqual(usr.id, "456")
        self.assertEqual(usr.created_at, dtm)
        self.assertEqual(usr.updated_at, dtm)

    def test_instantiation_with_args_and_kwargs(self):
        """Testing instantiation with both args and kwargs."""
        dtm = datetime.now()
        dtm_format = dtm.isoformat()
        usr = User(id="456", created_at=dtm_format, updated_at=dtm_format)
        self.assertEqual(usr.id, "456")
        self.assertEqual(usr.created_at, dtm)
        self.assertEqual(usr.updated_at, dtm)

    def test_instantiation_with_None_kwargs(self):
        """Testing instantiation with both args and kwargs."""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class Test_User_save(unittest.TestCase):
    """Unittests for testing the save method of the  class."""

    def setUp(self):
        """Renames the file.json if it exists before running tests."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

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

    def test_one_save(self):
        """Testing one save updates the updated_at attribute."""
        usr = User()
        sleep(0.05)
        updated_at_one = usr.updated_at
        usr.save()
        self.assertLess(updated_at_one, usr.updated_at)

    def test_two_saves(self):
        """Testing two saves have different updated_at values."""
        usr = User()
        sleep(0.05)
        updated_at_one = usr.updated_at
        usr.save()
        updated_at_two = usr.updated_at
        self.assertLess(updated_at_one, updated_at_two)
        sleep(0.05)
        usr.save()
        self.assertLess(updated_at_two, usr.updated_at)

    def test_save_with_arg(self):
        """Testing calling the save method with arguments raises a TypeError."""
        usr = User()
        with self.assertRaises(TypeError):
            usr.save(None)

    def test_save_updates_file(self):
        """Testing save method updates file.json."""
        usr = User()
        usr.save()
        usrid = "User." + usr.id
        with open("file.json", "r") as file:
            self.assertIn(usrid, file.read())


class Test_User_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        """Testing to_dict returns a dictionary."""
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_has_expected_keys(self):
        """Testing to_dict contains the expected keys.""" 
        usr = User()
        self.assertIn("id", usr.to_dict())
        self.assertIn("created_at", usr.to_dict())
        self.assertIn("updated_at", usr.to_dict())
        self.assertIn("__class__", usr.to_dict())

    def test_to_dict_has_added_attributes(self):
        """Testing to_dict contains added attributes."""
        usr = User()
        usr.middle_name = "Holberton"
        usr.my_number = 98
        self.assertEqual("Holberton", usr.middle_name)
        self.assertIn("my_number", usr.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Testing datetime attributes in to_dict are strings."""
        usr = User()
        usr_dict = usr.to_dict()
        self.assertEqual(str, type(usr_dict["id"]))
        self.assertEqual(str, type(usr_dict["created_at"]))
        self.assertEqual(str, type(usr_dict["updated_at"]))

    def test_to_dict_output(self):
        """Testing the output of to_dict matches expected dictionary."""
        dtm = datetime.today()
        usr = User()
        usr.id = "456789"
        usr.created_at = usr.updated_at = dtm
        tdict = {
            'id': '456789',
            '__class__': 'User',
            'created_at': dtm.isoformat(),
            'updated_at': dtm.isoformat(),
        }
        self.assertDictEqual(usr.to_dict(), tdict)

    def test_to_dict_contrast_with_dunder_dict(self):
        """Testing to_dict is not equal to __dict__."""
        usr = User()
        self.assertNotEqual(usr.to_dict(), usr.__dict__)

    def test_to_dict_with_arg(self):
        """Testing to_dict method raises TypeError when called with an argument."""
        usr = User()
        with self.assertRaises(TypeError):
            usr.to_dict(None)


if __name__ == "__main__":
    unittest.main()
