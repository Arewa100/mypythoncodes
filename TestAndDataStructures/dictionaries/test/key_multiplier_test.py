from unittest import TestCase
from dictionary import key_multiplier

class TestKeyMultiplier(TestCase):
    def test_key_multiplier_1(self):
        given_list = [1, 2, 3, 4, 5]
        expected_result = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
        self.assertEqual(key_multiplier.key_multiplier(given_list), expected_result)

    def test_key_multiplier_for_different_input(self):
        given_list = [2, 3, 2, 4, 5]
        expected_result = {2: 8, 3: 27, 2: 8, 4: 64, 5: 125}
        self.assertEqual(key_multiplier.key_multiplier(given_list), expected_result)
