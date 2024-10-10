from unittest import TestCase
from src.airconditional.air_condition import AirCondition

class TestForAc(TestCase):

    def test_that_there_is_an_ac(self):
        air_condition: AirCondition = AirCondition()
        self.assertEqual(isinstance(air_condition, AirCondition), True)

    def test_that_the_ac_is_off(self):
        air_condition: AirCondition = AirCondition()
        self.assertFalse(air_condition._is_on())

    def test_to_turn_on_ac_and_ac_will_be_on(self):
        air_condition: AirCondition = AirCondition()
        air_condition.turn_on()
        self.assertTrue(air_condition._is_on())

    def test_to_turn_off_ac_and_ac_will_be_off(self):
        air_condition: AirCondition = AirCondition()
        self.assertFalse(air_condition._is_on())
        air_condition.turn_on()
        self.assertTrue(air_condition._is_on())
        air_condition.turn_off()
        self.assertFalse(air_condition._is_on())

    def test_to_increase_temperature_of_ac_when_it_is_off(self):
        air_condition: AirCondition = AirCondition()
        self.assertFalse(air_condition._is_on())
        self.assertRaises(ValueError, air_condition.increase_temperature)

    def test_to_increase_temperature_of_ac_when_ac_is_on_temperature_is_increased(self):
        air_condition: AirCondition = AirCondition()
        self.assertFalse(air_condition._is_on())
        air_condition.turn_on()
        air_condition.increase_temperature()
        self.assertEqual(air_condition.temperature(), 17)

    def test_to_decrease_temperature_of_ac_when_ac_is_off(self):
        air_condition: AirCondition = AirCondition()
        self.assertFalse(air_condition._is_on())
        self.assertRaises(ValueError, air_condition.decrease_temperature)

    def test_to_decrease_temperature_of_ac_when_ac_is_on_temperature_is_decreased(self):
        air_condition: AirCondition = AirCondition()
        self.assertFalse(air_condition._is_on())
        air_condition.turn_on()
        air_condition.increase_temperature()
        self.assertEqual(air_condition.temperature(), 17)
        air_condition.decrease_temperature()
        self.assertEqual(air_condition.temperature(), 16)

    def test_to_increase_temperature_above_30_ac_should_maintain_temperature_to_be_30(self):
        air_condition: AirCondition = AirCondition()
        self.assertFalse(air_condition._is_on())
        air_condition.turn_on()
        for temp in range(35):
            air_condition.increase_temperature()
        self.assertEqual(air_condition.temperature(), 30)

    def test_to_decrease_temperature_below_16_ac_should_maintain_temperature_to_be_16(self):
        air_condition: AirCondition = AirCondition()
        self.assertFalse(air_condition._is_on())
        air_condition.turn_on()
        air_condition.increase_temperature()
        self.assertEqual(air_condition.temperature(), 17)
        air_condition.decrease_temperature()
        air_condition.decrease_temperature()
        air_condition.decrease_temperature()
        self.assertEqual(air_condition.temperature(), 16)


