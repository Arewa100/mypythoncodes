from unittest import TestCase

from dictionary import email_validator


class TestEmailValidator(TestCase):
    def test_password_validator(self):
        self.assertEqual(email_validator.email_validator("olasoyinmiracle@gmail.com"), True)

    def test_email_validator_if_it_is_can_test_for_wrong_email(self):
        self.assertRaises(ValueError, email_validator.email_validator, "olasoyinmm")

    def test_email_validator_if_it_is_can_test_for_wrong_with_numbers(self):
        self.assertRaises(ValueError, email_validator.email_validator, "1222@gamil.com")