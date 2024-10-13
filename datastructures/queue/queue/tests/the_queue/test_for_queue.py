from unittest import TestCase
from src.the_queue.queue import Queue


class TestQueue(TestCase):
    def setUp(self):
        self.queue = Queue(10)

    def test_to_create_instance_of_a_queue(self):
        self.assertEqual(isinstance(self.queue, Queue), True)

    def test_that_queue_is_empty(self):
        self.assertTrue(self.queue.is_empty_queue())

    def test_that_queue_is_full(self):
        self.assertFalse(self.queue.is_full_queue())

    def test_that_to_add_one_element_to_queue(self):
        self.queue.en_queue(10)
        self.assertFalse(self.queue.is_empty_queue())

    def test_that_to_add_10_elements_to_queue_and_check_if_it_is_full(self):
        for number in range(1, 11):
            self.queue.en_queue(number)
        self.assertTrue(self.queue.is_full_queue())

    def test_to_peek_element_at_the_front_of_queue(self):
        self.queue.en_queue(10)
        self.queue.en_queue(20)
        self.queue.en_queue(30)
        self.assertEqual(self.queue.front(), 10)

    def test_to_peek_back_element_in_the_queue(self):
        self.queue.en_queue(10)
        self.queue.en_queue(20)
        self.queue.en_queue(30)
        self.assertEqual(self.queue.back(), 30)

    def test_to_delete_element_from_queue(self):
        self.queue.en_queue(10)
        self.queue.en_queue(20)
        self.queue.en_queue(30)
        self.queue.en_queue(40)
        self.assertEqual(self.queue.front(), 10)
        self.queue.delete_queue()
        self.assertEqual(self.queue.back(), 40)

    def test_that_new_element_cannot_be_added_to_a_queue_when_it_is_full(self):
        for number in range(1, 11):
            self.queue.en_queue(number)

        self.assertRaises(IndexError, self.queue.en_queue, 12)

    def test_to_delete_element_when_queue_is_full(self):
        for number in range(1, 11):
            self.queue.en_queue(number)
        self.queue.delete_queue()
        self.assertEqual(self.queue.back(), 10)




