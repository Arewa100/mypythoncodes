from unittest import TestCase
from src.strings.character_swapper import character_swapper


class TestCaseForCharacterSwapper(TestCase):
    def test_that_character_swapper_exits(self):
        character_swapper('abc', 'xyz')

    def test_to_pass_two_arguments_abc_xyz_and_get_a_swapped_character_xyc_abz(self):
        self.assertEqual(character_swapper('abc', 'xyz'), 'xyc abz')

    def test_to_pass_cup_and_pop_and_get_pop_cup(self):
        self.assertEqual(character_swapper('cup', 'pop'), 'pop cup')
