from unittest import TestCase
from src.linkedlist.linked_list import LinkedList

class TestLinkedList(TestCase):
    def setUp(self):
        self.linked_list: LinkedList = LinkedList()

    def test_that_linked_list_exists(self):
        self.assertEqual(isinstance(self.linked_list, LinkedList), True)

    def test_that_linked_list_is_empty(self):
        self.assertTrue(self.linked_list.is_empty())

    def test_to_add_item_to_empty_linked_list(self):
        self.linked_list.insert(20)
        self.assertFalse(self.linked_list.is_empty())

    def test_to_add_to_item_to_the_linked_list(self):
        self.linked_list.insert(20)
        self.linked_list.insert(30)
        self.assertFalse(self.linked_list.is_empty())

    def test_to_check_the_first_element_in_the_linked_list(self):
        self.linked_list.insert(20)
        self.assertEqual(20, self.linked_list.front().get_data())

    def test_to_check_the_last_element_in_the_linked_list(self):
        self.linked_list.insert(20)
        self.assertEqual(self.linked_list.back().get_data(), 20)

    def test_to_insert_2_data_item_to_the_list_and_check_the_first_and_last(self):
        self.linked_list.insert(20)
        self.linked_list.insert(30)
        self.assertEqual(self.linked_list.front().get_data(), 20)
        self.assertEqual(self.linked_list.back().get_data(), 30)

    def test_to_insert_3_data_item_and_check_its_size(self):
        self.linked_list.insert(20)
        self.linked_list.insert(30)
        self.linked_list.insert(30)
        self.assertEqual(3, self.linked_list.size())

    def test_to_insert_item_at_a_specific_index(self):
        self.linked_list.insert(20)
        self.linked_list.insert(30)
        self.linked_list.insert(40)
        self.linked_list.insert_at(1, 50)
        self.assertEqual(self.linked_list.size(), 4)
        self.assertEqual(self.linked_list.front().get_linked_node().get_linked_node().get_data(), 50)

    def test_to_insert_at_start_head(self):
        self.linked_list.insert(20)
        self.linked_list.insert(30)
        self.linked_list.insert(40)
        self.linked_list.insert_at_start(18)
        self.assertEqual(self.linked_list.size(), 4)
        self.assertEqual(self.linked_list.front().get_data(), 18)

        self.assertEqual(self.linked_list.back().get_data(), 40)
        self.assertEqual(self.linked_list.front().get_linked_node().get_data(), 20)

    def test_to_destroy_the_linked_list(self):
        self.linked_list.insert(20)
        self.linked_list.insert(30)
        self.linked_list.insert(40)
        self.linked_list.destroy_list()
        self.assertIsNone(self.linked_list.front())

    def test_to_delete_from_a_specific_index(self):
        self.linked_list.insert(20)
        self.linked_list.insert(30)
        self.linked_list.insert(40)
        self.linked_list.insert(90)
        self.linked_list.delete(2)
        self.assertEqual(self.linked_list.size(), 3)

    def test_to_display_data_of_components_in_the_linked_list(self):
        self.linked_list.insert(20)
        self.linked_list.insert(30)
        self.linked_list.insert(40)
        self.linked_list.insert(90)
        expected_list = "[20, 30, 40, 90]"
        list_result = self.linked_list.display()
        self.assertEqual(list_result, expected_list)

    def test_that_item_can_be_searched_in_the_linked_list_result_is_boolean(self):
        self.linked_list.insert(20)
        self.linked_list.insert(30)
        self.linked_list.insert(40)
        self.linked_list.insert(90)
        self.assertTrue(self.linked_list.search(40))

    def test_to_search_item_that_is_not_in_the_linked_list_result_is_false(self):
        self.linked_list.insert(20)
        self.linked_list.insert(30)
        self.linked_list.insert(40)
        self.linked_list.insert(90)
        self.assertFalse(self.linked_list.search(18))
