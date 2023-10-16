#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
"""unittest module for testing Basemodel class"""
class TestBaseModel(unittest.TestCase):
    """shows several testcases for Basemodel"""

    def test_creation(self):
        # Test creating an instance and checking attributes
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertAlmostEqual((obj.updated_at - obj.created_at).total_seconds(), 0, places=2)

    def test_save_method(self):
        # Test the save method
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        # Test converting to dictionary
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_string_representation(self):
        # Test the string representation
        obj = BaseModel()
        obj_str = str(obj)
        self.assertTrue(obj_str.startswith('[BaseModel]'))
        self.assertIn(obj.id, obj_str)

    def test_unique_ids(self):
        # Test multiple instances with unique IDs
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_attribute_modification(self):
        # Test modifying attributes
        obj = BaseModel()
        initial_created_at = obj.created_at
        initial_updated_at = obj.updated_at
        obj.value = 42
        obj.save()
        self.assertEqual(obj.created_at, initial_created_at)
        self.assertNotEqual(obj.updated_at, initial_updated_at)

    def test_base_model_instance(self):
        self.base_model = BaseModel()
        self.assertIsInstance(self.base_model, BaseModel)

    def test_base_model_id(self):
        self.base_model = BaseModel()
        self.assertTrue(hasattr(self.base_model, 'id'))

    def test_base_model_created_at(self):
        self.base_model = BaseModel()
        self.assertTrue(hasattr(self.base_model, 'created_at'))

    def test_base_model_updated_at(self):
        self.base_model = BaseModel()
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

if __name__ == '__main__':
    unittest.main()
