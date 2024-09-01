from unittest import TestCase
from bank.account.account import Account


class TestAccount(TestCase):
    def setUp(self):
        self.account = Account("5555", "miracle", "olasoyin")

    def test_account_exists(self):
        self.account.account_number = "5555"

    def test_to_check_that_account_balance_is_zero(self):
        self.assertEqual(self.account.check_balance("5555", "0000"), 0)

    def test_to_deposit_2k_and_check_balance_to_be_2k(self):
        self.account.deposit("5555", 2000)
        self.assertEqual(self.account.check_balance("5555", "0000"), 2000)

    def test_to_deposit_2k_balance_is_2k_and_deposit_5k_balance_is_still_2k(self):
        self.account.deposit("5555", 2000)
        self.assertEqual(self.account.check_balance("5555", "0000"), 2000)
        self.account.deposit("5555", -5000)
        self.assertEqual(self.account.check_balance("5555", "0000"), 2000)

    def test_that_password_is_required_to_check_balance(self):
        self.account.deposit("5555", 2000)
        self.assertEqual(self.account.check_balance("5555", "0000"), 2000)

    def test_to_change_account_pin(self):
        self.account.deposit("5555", 2000)
        self.assertEqual(self.account.check_balance("5555", "0000"), 2000)
        self.account.update_pin("1222")
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)

    def test_to_change_pin_and_check_balance_with_the_old_pin(self):
        self.account.deposit("5555", 2000)
        self.assertEqual(self.account.check_balance("5555", "0000"), 2000)
        self.account.update_pin("1222")
        self.assertRaises(ValueError, self.account.check_balance,"5555", "0000")

    def test_to_raise_error_if_new_pin_is_updated_to_previous_pin(self):
        self.account.update_pin("1222")
        self.account.deposit("5555", 2000)
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)
        self.assertRaises(ValueError, self.account.update_pin, "1222")

    def test_to_deposit_only_when_account_number_is_valid(self):
        self.account.deposit("5555", 2000)
        self.assertEqual(self.account.check_balance("5555", "0000"), 2000)
        self.assertRaises(ValueError, self.account.deposit, "5455", 2000)


