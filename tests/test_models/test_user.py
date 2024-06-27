#!/usr/bin/python3
""" """
import os
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models.place import Place
from models.review import Review
from models import storage

class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "not testing db storage")
    def test_places_relationship_db(self):
        """Test relationship between User and Place in DBStorage"""
        new_user = self.value(email="test@test.com", password="test")
        new_user.save()
        new_place = Place(user_id=new_user.id, name="Test Place", city_id="0001")
        new_place.save()
        self.assertIn(new_place, new_user.places)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "not testing db storage")
    def test_reviews_relationship_db(self):
        """Test relationship between User and Review in DBStorage"""
        new_user = self.value(email="test@test.com", password="test")
        new_user.save()
        new_review = Review(user_id=new_user.id, text="Test Review", place_id="0001")
        new_review.save()
        self.assertIn(new_review, new_user.reviews)

if __name__ == "__main__":
    unittest.main()
