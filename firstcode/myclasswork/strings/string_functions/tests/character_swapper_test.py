from unittest import TestCase
from src.strings.character_functions import character_swapper
from src.strings.character_functions import character_placer
from strings.character_functions import word_sorter
from strings.character_functions import character_occurrence_checker


class TestCaseForCharacterSwapper(TestCase):
    def test_that_character_swapper_exists(self):
        character_swapper('abc', 'xyz')

    def test_to_pass_two_arguments_abc_xyz_and_get_a_swapped_character_xyc_abz(self):
        self.assertEqual(character_swapper('abc', 'xyz'), 'xyc abz')

    def test_to_pass_cup_and_pop_and_get_pop_cup(self):
        self.assertEqual(character_swapper('cup', 'pop'), 'pop cup')

    def test_to_pass_numbers_and_throw_exception(self):
        self.assertRaises(TypeError, character_swapper, 123, 'xyz')


class TestCaseForCharacterPlacer(TestCase):
    def test_that_character_placer_exists(self):
        character_placer('ce', 'hello')

    def test_to_take_argument_ce_and_helloo_and_return_helceloo(self):
        self.assertEqual(character_placer('ce', 'helloo'), 'helceloo')

    def test_to_take_argument_mapple_and_ce_and_return_mapceple(self):
        self.assertEqual(character_placer('ce', 'mapple'), 'mapceple')

class TestCaseForWordSorter(TestCase):
    def test_that_word_sorter_exists(self):
        word_sorter("SeMiColON")

    def test_that_word_sortter_can_rearrange_the_word_SeMiColON(self):
        self.assertEqual(word_sorter("SeMiColON"), "SMCONeiol")

class TestCaseForCharacterOccurrenceChecker(TestCase):
    def test_that_character_occurrence_checker_exists(self):
        character_occurrence_checker("semicolon", "o")

    def test_to_check_the_number_occurrence_of_e_in_semicolon(self):
        self.assertEqual(character_occurrence_checker("semicolon", "o"), ('o', 2))

    def test_