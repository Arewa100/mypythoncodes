from unittest import TestCase
from src.bike.bike import Bike


class TestBike(TestCase):
    def test_that_bike_exists(self):
        bike: Bike = Bike()
        self.assertEqual(isinstance(bike, Bike), True)

    def test_that_bike_off_normally(self):
        bike: Bike = Bike()
        self.assertFalse(bike.is_bike_on())

    def test_to_turn_bike_on_when_it_is_off(self):
        bike: Bike = Bike()
        bike.turn_on()
        self.assertTrue(bike.is_bike_on())

    def test_to_turn_bike_off_when_it_is_on(self):
        bike: Bike = Bike()
        self.assertFalse(bike.is_bike_on())
        bike.turn_on()
        self.assertTrue(bike.is_bike_on())
        bike.turn_off()
        self.assertFalse(bike.is_bike_on())

    def test_that_current_speed_off_bike_is_zero_when_it_is_off(self):
        bike: Bike = Bike()
        self.assertFalse(bike.is_bike_on())
        self.assertEqual(bike._bike_speed, 0)

    # def test_to_check_bike_gear_when_it_is_off(self):
    #     bike: Bike = Bike(1)
    #     self.assertEqual(bike._gear, "bike is off")


