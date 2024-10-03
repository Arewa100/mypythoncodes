from unittest import TestCase
from src.television.television import Tv


class TestTelevision(TestCase):
    def test_that_tv_exists(self):
       television = Tv()
       self.assertTrue(isinstance(television, Tv), True)

    def test_that_tv_is_off(self):
        television = Tv()
        self.assertFalse((television._is_on()))

    def test_to_on_tv_when_it_is_off(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.turn_on()
        self.assertTrue(television._is_on())

    def test_to_off_tv_when_it_is_on(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.turn_on()
        self.assertTrue(television._is_on())
        television.turn_off()
        self.assertFalse(television._is_on())

    def test_to_get_tv_channel_when_it_is_off(self):
        television = Tv()
        self.assertEqual(television.get_channel(), 0)

    def test_to_get_tv_channel_when_it_is_on(self):
        television = Tv()
        television.turn_on()
        self.assertEqual(television.get_channel(), 1)

    def test_to_set_channel_when_tv_is_off_expected_0(self):
        television = Tv()
        television.set_channel(2)
        self.assertEqual(television.get_channel(), 0)

    def test_to_set_channel_when_tv_is_on(self):
        television = Tv()
        television.turn_on()
        self.assertTrue(television._is_on())
        television.set_channel(2)
        self.assertEqual(television.get_channel(), 2)

    def test_to_get_volume_when_tv_is_off_expected_0(self):
        television = Tv()
        self.assertFalse(television._is_on())
        self.assertEqual(television.get_volume(), 0)

    def test_to_get_current_tv_volume_when_tv_is_on(self):
        television = Tv()
        television.turn_on()
        self.assertTrue(television._is_on())
        self.assertEqual(television.get_volume(), 0)

    def test_to_set_tv_volume_when_tv_is_off(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.set_volume(1)
        self.assertEqual(television.get_volume(), 0)

    def test_to_set_tv_volume_when_tv_is_on(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.turn_on()
        television.set_volume(2)
        self.assertEqual(television.get_volume(), 2)

    def test_to_increase_channel_when_tv_is_off_expecting_zero(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.channel_up()
        self.assertEqual(television.get_channel(), 0)

    def test_to_increase_channel_when_tv_is_on(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.turn_on()
        self.assertTrue(television._is_on())
        television.channel_up()
        self.assertEqual(television.get_channel(), 2)

    def test_to_increase_channel_more_when_tv_is_on(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.turn_on()
        self.assertTrue(television._is_on())
        television.channel_up()
        television.channel_up()
        television.channel_up()
        self.assertEqual(television.get_channel(), 4)

    def test_to_decrease_channel_when_tv_is_off_expecting_zero(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.channel_down()
        self.assertEqual(television.get_channel(), 0)

    def test_to_decrease_channel_when_tv_is_on_and_channel_is_increased(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.turn_on()
        self.assertTrue(television._is_on())
        television.channel_up()
        television.channel_up()
        self.assertEqual(television.get_channel(), 3)
        television.channel_down()
        self.assertEqual(television.get_channel(), 2)


    def test_to_decrease_channel_below_zero_when_tv_is_on(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.turn_on()
        television.channel_down()
        television.channel_down()
        self.assertEqual(television.get_channel(), 1)

    def test_to_increase_volume_when_tv_is_off_expecting_zero(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.volume_up()
        self.assertEqual(television.get_volume(), 0)

    def test_to_increase_volume_when_tv_is_on(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.turn_on()
        self.assertTrue(television._is_on())
        television.volume_up()
        self.assertEqual(television.get_volume(), 1)

    def test_to_increase_volume_more_when_tv_is_on(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.turn_on()
        self.assertTrue(television._is_on())
        television.volume_up()
        television.volume_up()
        self.assertEqual(television.get_volume(), 2)

    def test_to_decrease_volume_when_tv_is_off(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.volume_down()
        self.assertEqual(television.get_volume(), 0)

    def test_to_decrease_volume_when_tv_is_on_and_volume_is_increased(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.turn_on()
        television.volume_up()
        self.assertEqual(television.get_volume(), 1)
        television.volume_down()
        self.assertEqual(television.get_volume(), 0)

    def test_to_tv_volume_cannot_be_decreased_below_zero(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.turn_on()
        television.volume_up()
        self.assertEqual(television.get_volume(), 1)
        television.volume_down()
        television.volume_down()
        self.assertEqual(television.get_volume(), 0)


    def test_to_set_tv_channel_above_100(self):
        television = Tv()
        self.assertFalse(television._is_on())
        television.turn_on()
        television.set_channel(100)
        self.assertEqual(television.get_channel(), 100)
        television.set_channel(101)
        self.assertEqual(television.get_channel(), 100)