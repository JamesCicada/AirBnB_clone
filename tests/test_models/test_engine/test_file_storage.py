#!/usr/bin/python3
"""Unittest module to test the file storage module using the base_model module."""
import unittest
import models
from models.engine import file_storage
import pep8
import os


class TestFileStorage(unittest.TestCase):
    """Class that inherits from unittest to test the file storage module."""

    def setUp(self):
        """Method that initializes before each test."""
        self.new = models.BaseModel()

    def tearDown(self):
        """Method that runs after each test."""
        del self.new
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style(self):
        """Method to test the style of the file_storage module."""
        style = pep8.StyleGuide()
        result = style.check_files(['models/engine/file_storage.py'])
        errors = result.total_errors
        self.assertEqual(errors, 0, "fix pep8")

    def test_doc_module(self):
        """Method to test if the module has documentation."""
        doc = len(file_storage.__doc__.strip())
        self.assertTrue(doc > 0)
        doc = len(models.__init__.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_class(self):
        """Method to test if the class has documentation."""
        doc = len(file_storage.FileStorage.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_all_method(self):
        """Method to test if the 'all' method has documentation."""
        doc = len(file_storage.FileStorage.all.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_new_method(self):
        """Method to test if the 'new' method has documentation."""
        doc = len(file_storage.FileStorage.new.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_save_method(self):
        """Method to test if the 'save' method has documentation."""
        doc = len(file_storage.FileStorage.save.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_reload_method(self):
        """Method to test if the 'reload' method has documentation."""
        doc = len(file_storage.FileStorage.reload.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_file_path(self):
        """Test for the presence of the file."""
        self.new.x = "amgad"
        self.new.save()
        result = os.path.isfile('file.json')
        self.assertTrue(result)

    def test_object_attr(self):
        """Test object attribute instance."""
        all_obj = models.storage.all()
        self.assertTrue(isinstance(all_obj, dict))
        self.assertEqual(type(all_obj), dict)

    def test_has_attr(self):
        """Test for the presence of attributes."""
        self.assertTrue(hasattr(models.storage, "reload"))
        self.assertTrue(hasattr(models.storage, "all"))
        self.assertTrue(hasattr(models.storage, "new"))
        self.assertTrue(hasattr(models.storage, "save"))

    def test_instance(self):
        """Test if storage is an instance of FileStorage."""
        self.assertTrue(isinstance(models.storage,
                                   models.engine.file_storage.FileStorage))

    def test_check_save(self):
        """Check saving a 'new' instance of BaseModel."""
        all_obj = models.storage.all()
        new_obj = all_obj[f"BaseModel.{self.new.id}"]
        self.assertEqual(new_obj, self.new)

    def test_update_instance_save(self):
        """Method to test updating an instance and saving it."""
        self.new.name = "new"
        self.new.age = 10
        self.new.save()
        all_obj = models.storage.all()
        new_obj = all_obj[f"BaseModel.{self.new.id}"]
        self.assertEqual(new_obj, self.new)

    def test_new_instance(self):
        """Check new instance in storage."""
        new2 = models.BaseModel()
        all_obj = models.storage.all()
        new_obj = all_obj[f"BaseModel.{self.new.id}"]
        self.assertEqual(new_obj, self.new)
        new_obj = all_obj[f"BaseModel.{new2.id}"]
        self.assertEqual(new_obj, new2)


if __name__ == '__main__':
    unittest.main()