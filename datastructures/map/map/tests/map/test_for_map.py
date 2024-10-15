from unittest import TestCase
from src.map.map import Map

class TestMap(TestCase):
    def setUp(self):
        self.my_map:Map = Map()
    def test_that_map_has_been_created(self):
        self.assertEqual(isinstance(self.my_map, Map), True)

    def test_that_map_is_empty(self):
        self.assertEqual(self.my_map.size(), 0)

    def test_insert_key_value_pair_to_empty_map(self):
        self.assertEqual(self.my_map.size(), 0)
        self.my_map.insert("name", "miracle")
        self.assertEqual(self.my_map.size(), 1)

    def test_to_add_two_pairs_and_get_value_of_a_specific_key(self):
        self.my_map.insert("name1", "Miracle")
        self.my_map.insert("name2", "Bob")
        self.assertEqual(self.my_map.get("name2"), "Bob")

    def test_add_two_similar_keys_map_stores_only_one(self):
        self.my_map.insert("name1", "Miracle")
        self.my_map.insert("name1", "Bob")
        self.assertEqual(self.my_map.size(), 1)

    def test_that_key_is_not_in_a_map(self):
        self.my_map.insert("name1", "Miracle")
        self.my_map.insert("name2", "Bob")
        self.my_map.insert("name3", "Bob")
        self.assertFalse(self.my_map.contains("name4"))

    def test_that_key_is_in_map(self):
        self.my_map.insert("name1", "Miracle")
        self.my_map.insert("name2", "Bob")
        self.my_map.insert("name3", "Bob")
        self.assertTrue(self.my_map.contains("name2"))

    def test_to_update_value_of_a_particular_key(self):
        self.my_map.insert("name1", "Miracle")
        self.my_map.insert("name2", "Bob")
        self.my_map.insert("name3", "Bob")
        self.assertEqual(self.my_map.get("name2"), "Bob")
        self.my_map.update("name2", "kent")
        self.assertEqual(self.my_map.get("name2"), "kent")

    def test_to_delete_key_value_pair_of_a_map(self):
        self.my_map.insert("name1", "Miracle")
        self.my_map.insert("name2", "Bob")
        self.my_map.insert("name3", "kate")
        self.assertEqual(self.my_map.size(), 3)
        self.my_map.delete("name2")





