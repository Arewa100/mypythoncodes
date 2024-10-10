from unittest import TestCase
from src.bike.bike import Bike


class TestBike(TestCase):


    def test_that_bike_exists(self):
        bike: Bike = Bike()
        self.assertEqual(isinstance(bike, Bike), True)

    def test_that_bike_off_normally(self):
        bike: Bike = Bike()
        self.assertFalse(bike._is_bike_on())

    def test_to_turn_bike_on_when_it_is_off(self):
        bike: Bike = Bike()
        bike.turn_on()
        self.assertTrue(bike._is_bike_on())

    def test_to_turn_bike_off_when_it_is_on(self):
        bike: Bike = Bike()
        self.assertFalse(bike._is_bike_on())
        bike.turn_on()
        self.assertTrue(bike._is_bike_on())
        bike.turn_off()
        self.assertFalse(bike._is_bike_on())

    def test_that_current_speed_off_bike_is_zero_when_it_is_off(self):
        bike: Bike = Bike(1)
        self.assertFalse(bike._is_bike_on())
        self.assertEqual(bike._bike_speed(), 0)

    def test_to_check_bike_gear_when_it_is_off(self):
        bike: Bike = Bike(1)
        self.assertEqual(bike._gear, "bike is off")

    def test_to_check_bike_gear_when_it_is_on(self):
        bike: Bike = Bike(1)
        self.assertFalse(bike._is_bike_on())
        self.assertEqual(bike._gear, "bike is off")
        bike.turn_on()
        self.assertTrue(bike._is_bike_on())
        self.assertEqual(bike._gear, 1)

    def test_to_accelerate_bike_when_it_is_off(self):
        bike: Bike = Bike(1)
        self.assertFalse(bike._is_bike_on())
        self.assertEqual(bike._gear, "bike is off")
        self.assertRaises(ValueError, bike.accelerate)

    def test_to_accelerate_when_bike_is_on(self):
        bike: Bike = Bike(1)
        self.assertFalse(bike._is_bike_on())
        self.assertEqual(bike._gear, "bike is off")
        bike.turn_on()
        self.assertTrue(bike._is_bike_on())
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 1)

    def test_to_decelerate_bike_when_it_is_off(self):
        bike: Bike = Bike(1)
        self.assertFalse(bike._is_bike_on())
        self.assertEqual(bike._gear, "bike is off")
        self.assertRaises(ValueError, bike.decelerate)

    def test_to_accelerate_and_decelerate_bike_when_it_is_on(self):
        bike: Bike = Bike(1)
        self.assertFalse(bike._is_bike_on())
        bike.turn_on()
        self.assertTrue(bike._is_bike_on())
        self.assertEqual(bike._bike_speed(), 0)
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 1)
        bike.decelerate()
        self.assertEqual(bike._bike_speed(), 0)

    def test_to_decelerate_bike_speed_to_minimum_speed_which_is_zero(self):
        bike: Bike = Bike(1)
        self.assertFalse(bike._is_bike_on())
        bike.turn_on()
        self.assertTrue(bike._is_bike_on())
        bike.decelerate()
        self.assertEqual(bike._bike_speed(), 0)

    def test_to_accelerate_bike_at_gear_one_and_speed_should_increase_by_1_steps(self):
        bike: Bike = Bike(1)
        self.assertFalse(bike._is_bike_on())
        bike.turn_on()
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 1)
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 2)

    def test_to_accelerate_bike_until_gear_changes_to_gear_two_when_speed_is_21(self):
        bike: Bike = Bike()
        bike.turn_on()
        for acceleration in range(20):
            bike.accelerate()
        self.assertEqual(bike._bike_speed(), 20)
        self.assertEqual(bike._gear, 1)
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 21)
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 23)
        self.assertEqual(bike._gear, 2)
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 25)
        self.assertEqual(bike._gear, 2)

    def test_to_accelerate_bike_until_gear_changes_to_gear_three_when_speed_is_above_31(self):
        bike: Bike = Bike()
        bike.turn_on()
        for acceleration in range(26):
            bike.accelerate()
        self.assertEqual(bike._gear, 2)
        self.assertEqual(bike._bike_speed(), 31)
        bike.accelerate()
        self.assertEqual(bike._gear, 3)
        self.assertEqual(bike._bike_speed(), 34)
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 37)
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 40)
        self.assertEqual(bike._gear, 3)

    def test_to_accelerate_bike_until_gear_changes_to_gear_four_when_speed_is_above_41(self):
        bike: Bike = Bike()
        bike.turn_on()
        for acceleration in range(26):
            bike.accelerate()
        self.assertEqual(bike._gear, 2)
        self.assertEqual(bike._bike_speed(), 31)
        bike.accelerate()
        self.assertEqual(bike._gear, 3)
        self.assertEqual(bike._bike_speed(), 34)
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 37)
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 40)
        self.assertEqual(bike._gear, 3)
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 43)
        self.assertEqual(bike._gear, 3)
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 47)
        self.assertEqual(bike._gear, 4)

    def test_to_decelerate_bike_at_gear_one_and_speed_should_decrease_by_1_steps(self):
        bike: Bike = Bike(1)
        self.assertFalse(bike._is_bike_on())
        bike.turn_on()
        bike.accelerate()
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 2)
        bike.decelerate()
        self.assertEqual(bike._bike_speed(), 1)

    def test_to_decelerate_bike_at_gear_two(self):
        bike: Bike = Bike()
        bike.turn_on()
        for acceleration in range(20):
            bike.accelerate()
        self.assertEqual(bike._bike_speed(), 20)
        self.assertEqual(bike._gear, 1)
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 21)
        bike.accelerate()
        self.assertEqual(bike._bike_speed(), 23)
        self.assertEqual(bike._gear, 2)
        bike.decelerate()
        self.assertEqual(bike._bike_speed(), 21)
        self.assertEqual(bike._gear, 2)










