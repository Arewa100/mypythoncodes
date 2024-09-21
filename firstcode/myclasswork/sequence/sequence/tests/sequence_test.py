from ctypes import pydll
from unittest import TestCase
from src.sequence import sequence

class TestSequence(TestCase):
    def test_that_function_sequence_exists(self):
        self.assertTrue(sequence(34, 67, 55, 33, 12, 98), "['34', '67', '55', '33', '12', '98'], ('34', '67', '55', '33', '12', '98')")

    def test_that_function_can_return_tuple_and_list_of_given_arguments(self):
        self.assertEqual(sequence(34, 67, 55, 33, 12, 98), "['34', '67', '55', '33', '12', '98'], ('34', '67', '55', '33', '12', '98')")