from unittest import TestCase
from src.mystack.stack import Stack

class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack(10)

    def test_that_stack_exists(self):
        self.assertEqual(isinstance(self.stack, Stack), True)

    def test_that_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_that_stack_is_full(self):
        self.assertFalse(self.stack.is_full())

    def test_to_add_item_to_a_stack(self):
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())

    def test_to_add_ten_items_to_a_stack_and_confirm_if_it_is_full(self):
        for number in range(1, 11):
            self.stack.push(number)
        self.assertTrue(self.stack.is_full())

    def test_that_check_the_last_item_in_the_stack(self):
        self.stack.push(10)
        self.stack.push(9)
        self.stack.push(4)
        self.assertEqual(self.stack.peek(), 4)

    def test_that_to_remove_item_from_a_stack(self):
        self.stack.push(10)
        self.stack.push(9)
        self.stack.push(4)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 9)