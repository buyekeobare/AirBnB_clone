#!/usr/bin/python3
"""This script defines the unittests for models/place.py."""

import unittest
import models
import os
from models.place import Place
from datetime import datetime
from time import sleep


class Test_Place_instantiation(unittest.TestCase):
    """Unittests for testing the creation of the Place class instances."""

    def test_instantiates_no_args(self): 
        """Testing a Place instance can be instantiated with no arguments."""
        self.assertEqual(Place, type(Place()))

    def test_new_instance_in_objects(self):
        """Testing a new Place instance is stored in the objects dictionary."""
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Testing the id attribute is a public string."""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        """Testing the created_at attribute is a public datetime."""
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        """Testing the updated_at attribute is a public datetime."""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        """Testing city_id is a public class attribute of Place"""
        plc = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(plc))
        self.assertNotIn("city_id", plc.__dict__)

    def test_user_id_is_public_class_attribute(self):
        """Testing user_id is a public class attribute of Place."""
        plc = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(plc))
        self.assertNotIn("user_id", plc.__dict__)

    def test_name_is_public_class_attribute(self):
        """Testing the name is a public class attribute of Place."""
        plc = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(plc))
        self.assertNotIn("name", plc.__dict__)

    def test_description_is_public_class_attribute(self):
        """Testing the description is a public class attribute of Place."""
        plc = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(plc))
        self.assertNotIn("desctiption", plc.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        """Testing the number_rooms is a public class attribute of Place."""
        plc = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(plc))
        self.assertNotIn("number_rooms", plc.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        """Testing the number_bathrooms is a public class attribute of Place."""
        plc = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(plc))
        self.assertNotIn("number_bathrooms", plc.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        """Testing the max_guest is a public class attribute of Place."""
        plc = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(plc))
        self.assertNotIn("max_guest", plc.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        """Testing the price_by_night is a public class attribute of Place."""
        plc = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(plc))
        self.assertNotIn("price_by_night", plc.__dict__)

    def test_latitude_is_public_class_attribute(self):
        """Testing the latitude is a public class attribute of Place."""
        plc = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(plc))
        self.assertNotIn("latitude", plc.__dict__)

    def test_longitude_is_public_class_attribute(self):
        """Testing the longitude is a public class attribute of Place."""
        plc = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(plc))
        self.assertNotIn("longitude", plc.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        """Testing the amenity_ids is a public class attribute of Place."""
        plc = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(plc))
        self.assertNotIn("amenity_ids", plc.__dict__)

    def test_unique_ids_for_two_places(self):
        """Testing two places instances have unique ids."""
        plc1 = Place()
        plc2 = Place()
        self.assertNotEqual(plc1.id, plc2.id)

    def test_different_created_at_for_two_places (self):
        """Testing two places instances have different created_at values."""
        plc1 = Place()
        sleep(0.05)
        plc2 = Place()
        self.assertLess(plc1.created_at, plc2.created_at)

    def test_different_updated_at_two_places(self):
        """Testing two places instances have different updated_at values."""
        plc1 = Place()
        sleep(0.05)
        plc2 = Place()
        self.assertLess(plc1.updated_at, plc2.updated_at)

    def test_str_representation(self):
        """Testing the string representation of an class instance."""
        dtm = datetime.today()
        dtm_repr = repr(dtm)
        plc = Place()
        plc.id = "456789"
        plc.created_at = plc.updated_at = dtm
        plcstr = plc.__str__()
        self.assertIn("[Place] (456789)", plcstr)
        self.assertIn("'id': '456789'", plcstr)
        self.assertIn("'created_at': " + dtm_repr, plcstr)
        self.assertIn("'updated_at': " + dtm_repr, plcstr)

    def test_args_not_used(self):
        """Testing arguments not used do not affect instantiation."""
        plc = Place(None)
        self.assertNotIn(None, plc.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Testing instantiation with keyword arguments."""
        dtm = datetime.today()
        dtm_format = dtm.isoformat()
        plc = Place(id="456", created_at=dtm_format, updated_at=dtm_format)
        self.assertEqual(plc.id, "456")
        self.assertEqual(plc.created_at, dtm)
        self.assertEqual(plc.updated_at, dtm)

    def test_instantiation_with_args_and_kwargs(self):
        """Testing instantiation with both args and kwargs."""
        dtm = datetime.now()
        dtm_format = dtm.isoformat()
        plc = Place(id="456", created_at=dtm_format, updated_at=dtm_format)
        self.assertEqual(plc.id, "456")
        self.assertEqual(plc.created_at, dtm)
        self.assertEqual(plc.updated_at, dtm)

    def test_instantiation_with_None_kwargs(self):
        """Testing instantiation with None keyword arguments raises TypeError."""
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class Test_Place_save(unittest.TestCase):
    """Unittests for testing the save method of the Place class."""

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
        plc = Place()
        sleep(0.05)
        first_updated_at = plc.updated_at
        plc.save()
        self.assertLess(first_updated_at, plc.updated_at)

    def test_two_saves(self):
        """Testing two saves have different updated_at values."""
        plc = Place()
        sleep(0.05)
        first_updated_at = plc.updated_at
        plc.save()
        second_updated_at = plc.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        plc.save()
        self.assertLess(second_updated_at, plc.updated_at)

    def test_save_with_arg(self):
        """Testing calling the save method with arguments raises a TypeError."""
        plc = Place()
        with self.assertRaises(TypeError):
            plc.save(None)

    def test_save_updates_file(self):
        """Testing save method updates file.json."""
        plc = Place()
        plc.save()
        plcid = "Place." + plc.id
        with open("file.json", "r") as file:
            self.assertIn(plcid, file.read())


class Test_Place_to_dict(unittest.TestCase):
    """"Unittests for testing the to_dict method of the Place class"""

    def test_to_dict_type(self):
        """Testing to_dict returns a dictionary."""
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_has_expected_keys(self):
        """Testing to_dict contains the expected keys.""" 
        plc = Place()
        self.assertIn("id", plc.to_dict())
        self.assertIn("created_at", plc.to_dict())
        self.assertIn("updated_at", plc.to_dict())
        self.assertIn("__class__", plc.to_dict())

    def test_to_dict_has_added_attributes(self):
        """Testing to_dict contains added attributes."""
        plc = Place()
        plc.middle_name = "Holberton"
        plc.my_number = 98
        self.assertEqual("Holberton", plc.middle_name)
        self.assertIn("my_number", plc.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Testing datetime attributes in to_dict are strings."""
        plc = Place()
        plc_dict = plc.to_dict()
        self.assertEqual(str, type(plc_dict["id"]))
        self.assertEqual(str, type(plc_dict["created_at"]))
        self.assertEqual(str, type(plc_dict["updated_at"]))

    def test_to_dict_output(self):
        """Testing the output of to_dict matches expected dictionary."""
        dtm = datetime.today()
        plc = Place()
        plc.id = "456789"
        plc.created_at = plc.updated_at = dtm
        tdict = {
            'id': '456789',
            '__class__': 'Place',
            'created_at': dtm.isoformat(),
            'updated_at': dtm.isoformat(),
        }
        self.assertDictEqual(plc.to_dict(), tdict)

    def test_to_dict_contrast_with_dunder_dict(self):
        """Testing to_dict is not equal to __dict__."""
        plc = Place()
        self.assertNotEqual(plc.to_dict(), plc.__dict__)

    def test_to_dict_with_arg(self):
        """Testing to_dict method raises TypeError when called with an argument."""
        plc = Place()
        with self.assertRaises(TypeError):
            plc.to_dict(None)


if __name__ == "__main__":
    unittest.main()
