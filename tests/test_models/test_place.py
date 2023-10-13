import datetime
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    new = Place()
    attr_types = {
        'id': str,
        'created_at': datetime.datetime,
        'updated_at': datetime.datetime,
        'city_id': str,
        'user_id': str,
        'name': str,
        'description': str,
        'number_rooms': int,
        'number_bathrooms': int,
        'max_guest': int,
        'price_by_night': int,
        'latitude': float,
        'longitude': float,
        'amenity_ids': list
    }

    def setUp(self) -> None:
        super().setUp()

    def tearDown(self) -> None:
        super().tearDown()

    def assertAttributes(self, instance):
        """attributes data types"""
        self.assertIsInstance(instance, Place)
        self.assertTrue(issubclass(type(instance), BaseModel))

        attr = [
            'id', 'created_at', 'updated_at', 'city_id',
            'user_id', 'name', 'description', 'number_rooms',
            'max_guest', 'price_by_night', 'latitude', 'longitude', 'amenity_ids'
        ]
        for attr_name in attr:
            self.assertTrue(hasattr(instance, attr_name))
            self.assertIsInstance(getattr(instance, attr_name), self.attr_types[attr_name])

    def test_instantiation(self):
        """Test instantiation of Place class."""
        self.assertEqual(str(type(self.new)), "<class 'models.place.Place'>")
        self.assertIsInstance(self.new, Place)
        self.assertTrue(issubclass(type(self.new), BaseModel))
        self.assertAttributes(self.new)


if __name__ == '__main__':
    unittest.main()
