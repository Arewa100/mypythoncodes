from unittest import TestCase
from src.map.map import Map

class TestMap(TestCase):

    def test_that_map_has_been_created(self):
        my_map: Map = Map()
        self.assertEqual(isinstance(my_map, Map), True)