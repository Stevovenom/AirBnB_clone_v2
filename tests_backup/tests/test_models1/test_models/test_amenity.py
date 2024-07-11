#!/usr/bin/python3
""" """
import os
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.place import Place
from models import storage


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "not testing db storage")
    def test_place_amenities_relationship(self):
        """Test relationship between Amenity and Place in DBStorage"""
        new_amenity = self.value(name="TestAmenity")
        new_amenity.save()
        new_place = Place(name="TestPlace", user_id="1234", city_id="5678")
        new_place.amenities.append(new_amenity)
        new_place.save()
        self.assertIn(new_amenity, new_place.amenities)


if __name__ == "__main__":
    unittest.main()
