#!/usr/bin/python3
""" """
import os
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State
from models import storage


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "not testing db storage")
    def test_state_relationship_db(self):
        """Test relationship between City and State in DBStorage"""
        new_state = State(name="TestState")
        new_state.save()
        new_city = self.value(name="TestCity", state_id=new_state.id)
        new_city.save()
        self.assertEqual(new_city.state_id, new_state.id)
        self.assertIn(new_city, new_state.cities)


if __name__ == "__main__":
    unittest.main()
