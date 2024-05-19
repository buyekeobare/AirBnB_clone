#!/usr/bin/python3
"""This script defines the unittests for models/city.py."""

import unittest
import models
import os
from models.city import City
from datetime import datetime
from time import sleep

class Test_City_instantiation(unittest.TestCase):
    """Unittests for testing the creation of the City class instances."""

    def test_instantiation_no_args(self):
        """Testing a City instance can be instantiated with no arguments."""
        self.assertEqual(City, type(City()))

    def test_new_instance_in_objects(self):
        """Testing a new City instance is stored in the objects dictionary."""
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Testing the id attribute is a public string."""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        """Testing the created_at attribute is a public datetime."""
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        """Testing the updated_at attribute is a public datetime."""
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_attribute(self):
        """Testing state_id is a public class attribute of City"""
        ct = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(ct))
        self.assertNotIn("state_id", ct.__dict__)

    def test_name_is_public_attribute(self):
        """Testing the name is a public class attribute of City."""
        ct = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(ct))
        self.assertNotIn("name", ct.__dict__)

    def test_unique_ids_for_two_cities(self):
        """Testing two cities instances have unique ids."""
        ct1 = City()
        ct2 = City()
        self.assertNotEqual(ct1.id, ct2.id)

    def test_different_created_at_for_two_cities(self):
        """Testing two cities instances have different created_at values."""
        ct1 = City()
        sleep(0.05)
        ct2 = City()
        self.assertLess(ct1.created_at, ct2.created_at)

    def test_different_updated_at_for_two_cities(self):
        """Testing two cities instances have different updated_at values."""
        ct1 = City()
        sleep(0.05)
        ct2 = City()
        self.assertLess(ct1.updated_at, ct2.updated_at)

    def test_str_representation(self):
        """Testing the string representation of an class instance."""
        dtm = datetime.today()
        dtm_repr = repr(dtm)
        ct = City()
        ct.id = "456789"
        ct.created_at = ct.updated_at = dtm
        ctstr = ct.__str__()
        self.assertIn("[City] (456789)", ctstr)
        self.assertIn("'id': '456789'", ctstr)
        self.assertIn("'created_at': " + dtm_repr, ctstr)
        self.assertIn("'updated_at': " + dtm_repr, ctstr)

    def test_args_not_used(self):
        """Testing arguments not used do not affect instantiation."""
        ct = City(None)
        self.assertNotIn(None, ct.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Testing instantiation with keyword arguments."""
        dtm = datetime.today()
        dtm_format = dtm.isoformat()
        ct = City(id="456", created_at=dtm_format, updated_at=dtm_format)
        self.assertEqual(ct.id, "456")
        self.assertEqual(ct.created_at, dtm)
        self.assertEqual(ct.updated_at, dtm)

    def test_instantiation_with_args_and_kwargs(self):
        """Testing instantiation with both args and kwargs."""
        dtm = datetime.now()
        dtm_format = dtm.isoformat()
        ct = City(id="456", created_at=dtm_format, updated_at=dtm_format)
        self.assertEqual(ct.id, "456")
        self.assertEqual(ct.created_at, dtm)
        self.assertEqual(ct.updated_at, dtm)

    def test_instantiation_with_None_kwargs(self):
        """Testing instantiation with None keyword arguments raises TypeError."""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class Test_City_save(unittest.TestCase):
    """Unittests for the save method of the City class."""

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
        ct = City()
        sleep(0.05)
        updated_at_one = ct.updated_at
        ct.save()
        self.assertLess(updated_at_one, ct.updated_at)

    def test_two_saves(self):
        """Testing two saves have different updated_at values."""
        ct = City()
        sleep(0.05)
        updated_at_one = ct.updated_at
        ct.save()
        updated_at_two = ct.updated_at
        self.assertLess(updated_at_one, updated_at_two)
        sleep(0.05)
        ct.save()
        self.assertLess(updated_at_two, ct.updated_at)

    def test_save_with_arguments(self):
        """Testing calling the save method with arguments raises a TypeError."""
        ct = City()
        with self.assertRaises(TypeError):
            ct.save(None)

    def test_save_updates_file(self):
        """Testing save method updates file.json."""
        ct = City()
        ct.save()
        ctid = "City." + ct.id
        with open("file.json", "r") as file:
            self.assertIn(ctid, file.read())


class Test_City_to_dict(unittest.TestCase):
    """Unittests for testing the to_dict method of the City class"""

    def test_to_dict_type(self):
        """Testing to_dict returns a dictionary."""
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_has_expected_keys(self):
        """Testing to_dict contains the expected keys."""
        ct = City()
        self.assertIn("id", ct.to_dict())
        self.assertIn("created_at", ct.to_dict())
        self.assertIn("updated_at", ct.to_dict())
        self.assertIn("__class__", ct.to_dict())

    def test_to_dict_has_added_attributes(self):
        """Testing to_dict contains added attributes."""
        ct = City()
        ct.middle_name = "Holberton"
        ct.my_number = 98
        self.assertEqual("Holberton", ct.middle_name)
        self.assertIn("my_number", ct.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Testing datetime attributes in to_dict are strings."""
        ct = City()
        ct_dict = ct.to_dict()
        self.assertEqual(str, type(ct_dict["id"]))
        self.assertEqual(str, type(ct_dict["created_at"]))
        self.assertEqual(str, type(ct_dict["updated_at"]))

    def test_to_dict_output(self):
        """Testing the output of to_dict matches expected dictionary."""
        dtm = datetime.today()
        ct = City()
        ct.id = "456789"
        ct.created_at = ct.updated_at = dtm
        tdict = {
            'id': '456789',
            '__class__': 'City',
            'created_at': dtm.isoformat(),
            'updated_at': dtm.isoformat(),
        }
        self.assertDictEqual(ct.to_dict(), tdict)

    def test_to_dict_contrast_with_dunder_dict(self):
        """Testing to_dict is not equal to __dict__."""
        ct = City()
        self.assertNotEqual(ct.to_dict(), ct.__dict__)

    def test_to_dict_with_arg(self):
        """Testing to_dict method raises TypeError when called with an argument."""
        ct = City()
        with self.assertRaises(TypeError):
            ct.to_dict(None)


if __name__ == "__main__":
    unittest.main()
