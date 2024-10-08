from unittest import TestCase
from src.strings.character_functions import character_swapper, character_placer, word_sorter, character_occurrence_checker, special_character_remover

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

    def test_that_word_sortter_can_rearrange_the_word_HannAH(self):
        self.assertEqual(word_sorter("HannAH"), "HAHann")



class TestCaseForCharacterOccurrenceChecker(TestCase):
    def test_that_character_occurrence_checker_exists(self):
        character_occurrence_checker("semicolon", "o")

    def test_to_check_the_number_occurrence_of_e_in_semicolon(self):
        self.assertEqual(character_occurrence_checker("semicolon", "o"), ('o', 2))

    def test_to_check_the_number_occurrence_of_a_in_hanna(self):
        self.assertEqual(character_occurrence_checker("hanna", "a"), ('a', 2))


class TestCaseForSpecialCharacterRemover(TestCase):
    def test_that_special_character_remover_exists(self):
        special_character_remover("he,ll.o")

    def test_that_function_can_remove_special_character_from_input(self):
        self.assertEqual(special_character_remover("he,ll.o"), "hello")

    def test_that_function_can_remove_special_character_from_input2(self):
        self.assertEqual(special_character_remover("ja..ck"), "jack")