#!/usr/bin/python3
""" """
import os
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.amenity import Amenity
from models import storage

class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "not testing db storage")
    def test_amenities_db(self):
        """Test the Many-to-Many relationship between Place and Amenity in DBStorage"""
        new_place = self.value(name="Test Place")
        new_place.save()
        new_amenity1 = Amenity(name="Test Amenity 1")
        new_amenity1.save()
        new_amenity2 = Amenity(name="Test Amenity 2")
        new_amenity2.save()
        new_place.amenities.append(new_amenity1)
        new_place.amenities.append(new_amenity2)
        storage.save()
        self.assertIn(new_amenity1, new_place.amenities)
        self.assertIn(new_amenity2, new_place.amenities)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "not testing file storage")
    def test_amenities_fs(self):
        """Test the Many-to-Many relationship between Place and Amenity in FileStorage"""
        new_place = self.value(name="Test Place")
        new_place.save()
        new_amenity1 = Amenity(name="Test Amenity 1")
        new_amenity1.save()
        new_amenity2 = Amenity(name="Test Amenity 2")
        new_amenity2.save()
        new_place.amenities = new_amenity1
        new_place.amenities = new_amenity2
        storage.save()
        self.assertIn(new_amenity1.id, new_place.amenity_ids)
        self.assertIn(new_amenity2.id, new_place.amenity_ids)
        self.assertIn(new_amenity1, new_place.amenities)
        self.assertIn(new_amenity2, new_place.amenities)
