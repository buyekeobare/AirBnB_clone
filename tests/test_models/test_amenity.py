#!/usr/bin/python3
"""This script defines the unittests for models/amenity.py."""

import unittest
import models
import os
from models.amenity import Amenity
from datetime import datetime
from time import sleep

class Test_Amenity_Instantiation(unittest.TestCase):
    """Unittests for testing the creation of the Amenity class instances."""

    def test_instantiates_no_args(self):
        """Testing the Amenity can be instantiated with no arguments."""
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_in_objects(self):
        """Testing a new Amenity instance is stored in the objects dictionary."""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Testing the id attribute is a public string."""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self): 
        """Testing the created_at attribute is a public datetime."""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        """Testing the updated_at attribute is a public datetime."""
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_attribute(self):
        """Testing the name is a public class attribute of Amenity."""
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_unique_ids_for_two_amenities(self):
        """Testing two Amenity instances have unique ids."""
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_different_created_at_for_two_amenities(self):
        """Testing two Amenity instances have different created_at values."""
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_different_updated_at_for_two_amenities(self):
        """Testing two Amenity instances have different updated_at values."""
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_str_representation(self):
        """Testing the string representation of an Amenity instance."""
        dtm = datetime.today()
        dtm_repr = repr(dtm)
        am = Amenity()
        am.id = "456789"
        am.created_at = am.updated_at = dtm
        amstr = am.__str__()
        self.assertIn("[Amenity] (456789)", amstr)
        self.assertIn("'id': '456789'", amstr)
        self.assertIn("'created_at': " + dtm_repr, amstr)
        self.assertIn("'updated_at': " + dtm_repr, amstr)

    def test_args_not_used(self):
        """Testing arguments not used do not affect instantiation."""
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Testing instantiation with keyword arguments."""
        dtm = datetime.today()
        dtm_format = dtm.isoformat()
        am = Amenity(id="456", created_at=dtm_format, updated_at=dtm_format)
        self.assertEqual(am.id, "456")
        self.assertEqual(am.created_at, dtm)
        self.assertEqual(am.updated_at, dtm)

    def test_instantiation_with_args_and_kwargs(self):
        """Testing instantiation with both args and kwargs."""
        dtm = datetime.now()
        dtm_format = dtm.isoformat()
        am = Amenity(id="456", created_at=dtm_format, updated_at=dtm_format)
        self.assertEqual(am.id, "456")
        self.assertEqual(am.created_at, dtm)
        self.assertEqual(am.updated_at, dtm)

    def test_instantiation_with_None_kwargs(self):
        """Testing instantiation with None keyword arguments raises TypeError."""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

class Test_Amenity_save(unittest.TestCase):
    """Unittests for testing the save functionality of the Amenity class."""

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
        am = Amenity()
        sleep(0.05)
        updated_at_one = am.updated_at
        am.save()
        self.assertLess(updated_at_one, am.updated_at)

    def test_two_saves(self):
        """Testing two saves have different updated_at values."""
        am = Amenity()
        sleep(0.05)
        updated_at_one = am.updated_at
        am.save()
        updated_at_two = am.updated_at
        self.assertLess(updated_at_one, updated_at_two)
        sleep(0.05)
        am.save()
        self.assertLess(updated_at_two, am.updated_at)

    def test_save_with_arg(self):
        """Testing calling the save method with arguments raises a TypeError."""
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        """Testing save method updates file.json."""
        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("file.json", "r") as file:
            self.assertIn(amid, file.read())


class Test_Amenity_to_dict(unittest.TestCase):
    """Unittests for testing the to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        """Testing to_dict returns a dictionary."""
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_has_expected_keys(self):
        """Testing to_dict contains the expected keys."""
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_has_added_attributes(self):
        """Testing to_dict contains added attributes."""
        am = Amenity()
        am.middle_name = "Holberton"
        am.my_number = 98
        self.assertEqual("Holberton", am.middle_name)
        self.assertIn("my_number", am.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Testing datetime attributes in to_dict are strings."""
        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        """Testing the output of to_dict matches expected dictionary."""
        dtm = datetime.today()
        am = Amenity()
        am.id = "456789"
        am.created_at = am.updated_at = dtm
        tdict = {
            'id': '456789',
            '__class__': 'Amenity',
            'created_at': dtm.isoformat(),
            'updated_at': dtm.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), tdict)

    def test_to_dict_contrast_with_dunder_dict(self):
        """Testing to_dict is not equal to __dict__."""
        am = Amenity()
        self.assertNotEqual(am.to_dict(), am.__dict__)

    def test_to_dict_with_arg(self):
        """Testing to_dict method raises TypeError when called with an argument."""
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)


if __name__ == "__main__":
    unittest.main()
