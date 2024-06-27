#!/usr/bin/python3
""" """
import os
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.city import City
from models import storage

class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "not testing db storage")
    def test_cities_relationship_db(self):
        """Test relationship between State and City in DBStorage"""
        new_state = self.value(name="Test State")
        new_state.save()
        new_city = City(name="Test City", state_id=new_state.id)
        new_city.save()
        self.assertIn(new_city, new_state.cities)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "not testing file storage")
    def test_cities_relationship_fs(self):
        """Test relationship between State and City in FileStorage"""
        new_state = self.value(name="Test State")
        new_state.save()
        new_city = City(name="Test City", state_id=new_state.id)
        new_city.save()
        self.assertIn(new_city, new_state.cities)

if __name__ == "__main__":
    unittest.main()
