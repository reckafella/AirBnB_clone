#!/usr/bin/python3

"""
Module contains test cases for the BaseModel
"""
import unittest
from models.base_model import BaseModel
import models.base_model as bs_model


class TestBaseModel(unittest.TestCase):
    """
    class implements test cases for the base model
    """
    def test_base_model_docs(self):
        """
        Tests for Base Model docs
        """
        docs = bs_model.__doc__
        self.assertTrue(len(docs) > 1)
        self.assertTrue(len(BaseModel.__doc__) > 1)

    def test_base_model_attrs(self):
        """
        Tests for Base Model attributes
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertTrue(hasattr(bm1, 'id'))
        self.assertTrue(hasattr(bm1, 'created_at'))
        self.assertTrue(hasattr(bm1, 'updated_at'))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm2.id, str)
