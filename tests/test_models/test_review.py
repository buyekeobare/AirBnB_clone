#!/usr/bin/python3
"""This script defines the unittests for models/review.py."""

import unittest
import models
import os
from models.review import Review
from datetime import datetime
from time import sleep


class Test_Review_instantiation(unittest.TestCase):
    """Unittests for testing the creation of the Review class instances."""

    def test_instantiates_no_args(self):
        """Testing a Place instance can be instantiated with no arguments."""
        self.assertEqual(Review, type(Review()))

    def test_new_instance_in_objects(self):
        """Testing a new Place instance is stored in the objects dictionary."""
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Testing the id attribute is a public string."""
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        """Testing the created_at attribute is a public datetime."""
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        """Testing the updated_at attribute is a public datetime."""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        """Testing place_id is a public class attribute of Review"""
        rev = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rev))
        self.assertNotIn("place_id", rev.__dict__)

    def test_user_id_is_public_class_attribute(self):
        """Testing user_id is a public class attribute of Review."""
        rev = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rev))
        self.assertNotIn("user_id", rev.__dict__)

    def test_text_is_public_class_attribute(self):
        """Testing text is a public class attribute of Review."""
        rev = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rev))
        self.assertNotIn("text", rev.__dict__)

    def test_unique_ids_for_two_reviews(self):
        """Testing two places instances have unique ids."""
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

    def test_different_created_at_for_two_reviews(self):
        """Testing two places instances have different created_at values."""
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.created_at, rev2.created_at)

    def test_different_updated_at_for_two_reviews(self):
        """Testing two places instances have different updated_at values."""
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.updated_at, rev2.updated_at)

    def test_str_representation(self):
        """Testing the string representation of an class instance."""
        dtm = datetime.today()
        dtm_repr = repr(dtm)
        rev = Review()
        rev.id = "456789"
        rev.created_at = rev.updated_at = dtm
        revstr = rev.__str__()
        self.assertIn("[Review] (456789)", revstr)
        self.assertIn("'id': '456789'", revstr)
        self.assertIn("'created_at': " + dtm_repr, revstr)
        self.assertIn("'updated_at': " + dtm_repr, revstr)

    def test_args_not_used(self):
        """Testing arguments not used do not affect instantiation."""
        rev = Review(None)
        self.assertNotIn(None, rev.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Testing instantiation with keyword arguments."""
        dtm = datetime.today()
        dtm_format = dtm.isoformat()
        rev = Review(id="456", created_at=dtm_format, updated_at=dtm_format)
        self.assertEqual(rev.id, "456")
        self.assertEqual(rev.created_at, dtm)
        self.assertEqual(rev.updated_at, dtm)

    def test_instantiation_with_args_and_kwargs(self):
        """Testing instantiation with both args and kwargs."""
        dtm = datetime.now()
        dtm_format = dtm.isoformat()
        st = Review(id="456", created_at=dtm_format, updated_at=dtm_format)
        self.assertEqual(st.id, "456")
        self.assertEqual(st.created_at, dtm)
        self.assertEqual(st.updated_at, dtm)

    def test_instantiation_with_None_kwargs(self):
        """Testing instantiation with None keyword arguments raises TypeError."""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class Test_Review_save(unittest.TestCase):
    """Unittests for testing the save method of the Review class."""

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
        rev = Review()
        sleep(0.05)
        updated_at_one = rev.updated_at
        rev.save()
        self.assertLess(updated_at_one, rev.updated_at)

    def test_two_saves(self):
        """Testing two saves have different updated_at values."""
        rev = Review()
        sleep(0.05)
        updated_at_one = rev.updated_at
        rev.save()
        updated_at_two = rev.updated_at
        self.assertLess(updated_at_one, updated_at_two)
        sleep(0.05)
        rev.save()
        self.assertLess(updated_at_two, rev.updated_at)

    def test_save_with_arg(self):
        """Testing calling the save method with arguments raises a TypeError."""
        rev = Review()
        with self.assertRaises(TypeError):
            rev.save(None)

    def test_save_updates_file(self):
        """Testing save method updates file.json."""
        rev = Review()
        rev.save()
        revid = "Review." + rev.id
        with open("file.json", "r") as file:
            self.assertIn(revid, file.read())


class Test_Review_to_dict(unittest.TestCase):
    """"Unittests for testing the to_dict method of the Review class"""

    def test_to_dict_type(self):
        """Testing to_dict returns a dictionary."""
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_has_expected_keys(self):
        """Testing to_dict contains the expected keys.""" 
        rev = Review()
        self.assertIn("id", rev.to_dict())
        self.assertIn("created_at", rev.to_dict())
        self.assertIn("updated_at", rev.to_dict())
        self.assertIn("__class__", rev.to_dict())

    def test_to_dict_has_added_attributes(self):
        """Testing to_dict contains added attributes."""
        rev = Review()
        rev.middle_name = "Holberton"
        rev.my_number = 98
        self.assertEqual("Holberton", rev.middle_name)
        self.assertIn("my_number", rev.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Testing datetime attributes in to_dict are strings."""
        rev = Review()
        rev_dict = rev.to_dict()
        self.assertEqual(str, type(rev_dict["id"]))
        self.assertEqual(str, type(rev_dict["created_at"]))
        self.assertEqual(str, type(rev_dict["updated_at"]))

    def test_to_dict_output(self):
        """Testing the output of to_dict matches expected dictionary."""
        dtm = datetime.today()
        rev = Review()
        rev.id = "456789"
        rev.created_at = rev.updated_at = dtm
        tdict = {
            'id': '456789',
            '__class__': 'Review',
            'created_at': dtm.isoformat(),
            'updated_at': dtm.isoformat(),
        }
        self.assertDictEqual(rev.to_dict(), tdict)

    def test_to_dict_contrast_with_dunder_dict(self):
        """Testing to_dict is not equal to __dict__."""
        rev = Review()
        self.assertNotEqual(rev.to_dict(), rev.__dict__)

    def test_to_dict_with_arg(self):
        """Testing to_dict method raises TypeError when called with an argument."""
        rev = Review()
        with self.assertRaises(TypeError):
            rev.to_dict(None)


if __name__ == "__main__":
    unittest.main()
