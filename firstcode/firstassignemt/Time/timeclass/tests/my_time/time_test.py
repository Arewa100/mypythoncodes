from unittest import TestCase
from src.my_time.time import MyTime

class TestTime(TestCase):
    def test_that_time_object_exists(self):
        time = MyTime()
        self.assertTrue((isinstance(time, MyTime)), "time object is a Time object")

    def test_that_the_time_object_can_initialize_the_hour_minute_second(self):
        time = MyTime(10, 10, 10)
        self.assertEqual(time.hours, 10)
        self.assertEqual(time.minutes, 10)
        self.assertEqual(time.second, 10)

    def test_to_initialize_the_time_hour_attributes_wrongly(self):
        time =  MyTime(20, 10, 40)


    def test_to_initialize_the_time_minute_attributes_wrongly(self):
        self.assertRaises(ValueError, MyTime, 2, 70, 70)

    def test_to_initialize_the_time_second_attributes_wrongly(self):
        self.assertRaises(ValueError, MyTime, 7, 20, 70)





