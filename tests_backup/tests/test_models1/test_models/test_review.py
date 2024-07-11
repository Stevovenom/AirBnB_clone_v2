#!/usr/bin/python3
""" """
import os
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models.user import User
from models.place import Place
from models import storage

class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "not testing db storage")
    def test_place_relationship_db(self):
        """Test relationship between Review and Place in DBStorage"""
        new_place = Place(name="Test Place")
        new_place.save()
        new_review = self.value(text="Great place!", place_id=new_place.id, user_id="1234")
        new_review.save()
        self.assertIn(new_review, new_place.reviews)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "not testing db storage")
    def test_user_relationship_db(self):
        """Test relationship between Review and User in DBStorage"""
        new_user = User(email="test@test.com", password="password")
        new_user.save()
        new_review = self.value(text="Great place!", place_id="1234", user_id=new_user.id)
        new_review.save()
        self.assertIn(new_review, new_user.reviews)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "not testing file storage")
    def test_place_relationship_fs(self):
        """Test relationship between Review and Place in FileStorage"""
        new_place = Place(name="Test Place")
        new_place.save()
        new_review = self.value(text="Great place!", place_id=new_place.id, user_id="1234")
        new_review.save()
        self.assertIn(new_review.id, [review.id for review in new_place.reviews])

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "not testing file storage")
    def test_user_relationship_fs(self):
        """Test relationship between Review and User in FileStorage"""
        new_user = User(email="test@test.com", password="password")
        new_user.save()
        new_review = self.value(text="Great place!", place_id="1234", user_id=new_user.id)
        new_review.save()
        self.assertIn(new_review.id, [review.id for review in new_user.reviews])
