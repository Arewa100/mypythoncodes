from unittest import TestCase
from src.functions.word_splitter import word_splitter


class TestWordSplitter(TestCase):
    def test_that_word_splitter_exits(self):
        word_splitter("test")

    def test_word_splitter(self):
        self.assertEqual(word_splitter("hannah"), {'h': 2, 'a': 2, 'n': 2})
        self.assertEqual(word_splitter('awee'), {'a': 1, 'w': 1, 'e': 2})

    def test_that_word_splitter_can_split_another_word_and_return_its_key_value_pairs(self):
        self.assertEqual(word_splitter("semicolon"), {'s': 1, 'e': 1, 'm': 1, 'i': 1, 'c': 1, 'o': 2, 'l': 1, 'n': 1})

    def test_that_word_splitter_ignore_case(self):
        self.assertEqual(word_splitter("aweE"), {'a': 1, 'w': 1, 'e': 2})

    def test_that_word_cannot_be_a_number(self):
        self.assertRaises(TypeError, word_splitter, 5333)


