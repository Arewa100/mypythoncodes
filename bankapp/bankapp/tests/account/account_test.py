from unittest import TestCase
from bank.account.account import Account


class TestAccount(TestCase):
    def setUp(self):
        self.account = Account("5555", "miracle", "olasoyin")

    def test_account_exists(self):
        self.account.account_number = "5555"

    def test_to_check_that_account_balance_is_zero(self):
        self.account.update_pin("1222")
        self.assertEqual(self.account.check_balance("5555", "1222"), 0)

    def test_to_deposit_2k_and_check_balance_to_be_2k(self):
        self.account.deposit("5555", 2000)
        self.account.update_pin("1222")
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)

    def test_to_deposit_2k_balance_is_2k_and_deposit_5k_balance_is_still_2k(self):
        self.account.deposit("5555", 2000)
        self.account.update_pin("1222")
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)
        self.assertRaises(ValueError, self.account.deposit, "5555", -5000)
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)

    def test_that_password_is_required_to_check_balance(self):
        self.account.deposit("5555", 2000)
        self.account.update_pin("1222")
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)

    def test_to_change_account_pin(self):
        self.account.deposit("5555", 2000)
        self.account.update_pin("1222")
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)
        self.account.update_pin("1223")
        self.assertEqual(self.account.check_balance("5555", "1223"), 2000)

    def test_to_change_pin_and_check_balance_with_the_old_pin(self):
        self.account.deposit("5555", 2000)
        self.account.update_pin("1222")
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)
        self.account.update_pin("1223")
        self.assertRaises(ValueError, self.account.check_balance,"5555", "1222")

    def test_to_raise_error_if_new_pin_is_updated_to_previous_pin(self):
        self.account.update_pin("1222")
        self.account.deposit("5555", 2000)
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)
        self.assertRaises(ValueError, self.account.update_pin, "1222")

    def test_to_deposit_only_when_account_number_is_not_valid(self):
        self.account.deposit("5555", 2000)
        self.account.update_pin("1222")
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)
        self.assertRaises(ValueError, self.account.deposit, "5545", 2000)

    def test_that_length_of_pin_must_be_four(self):
        self.account.deposit("5555", 2000)
        self.account.update_pin("1222")
        self.assertRaises(ValueError,  self.account.update_pin, "1222")

    def test_that_to_check_balance_or_update_pin_the_default_pin_must_be_changed(self):
        self.account.deposit("5555", 2000)
        self.assertRaises(ValueError, self.account.check_balance, "5555", "0000")
        self.account.update_pin("1222")
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)

    def test_to_deposit_10k_and_withdraw_5k_balance_5k(self):
        self.account.update_pin("1222")
        self.account.deposit("5555", 10000)
        self.assertEqual(self.account.check_balance("5555", "1222"), 10000)
        self.account.withdraw("5555", 5000, "1222")
        self.assertEqual(self.account.check_balance("5555", "1222"), 5000)

    def test_to_deposit_10k_withdraw_2k_and_balance_is_8k(self):
        self.account.update_pin("1222")
        self.account.deposit("5555", 10000)
        self.assertEqual(self.account.check_balance("5555", "1222"), 10000)
        self.account.withdraw("5555", 2000, "1222")
        self.assertEqual(self.account.check_balance("5555", "1222"), 8000)

    def test_deposit_2k_and_withdraw_5k_balance_2k(self):
        self.account.update_pin("1222")
        self.account.deposit("5555", 2000)
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)
        self.assertRaises(ValueError, self.account.withdraw, "5545", 5000, "1122")
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)

    def test_to_deposit_2k_and_withdraw_minus_2k_and_balance_is_2k(self):
        self.account.update_pin("1222")
        self.account.deposit("5555", 2000)
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)
        self.assertRaises(ValueError, self.account.withdraw, "5555", -2000, "1122")
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)

    def test_to_confirm_account_number_and_pin_before_withdrawal(self):
        self.account.update_pin("1222")
        self.account.deposit("5555", 2000)
        self.assertEqual(self.account.check_balance("5555", "1222"), 2000)
        self.assertRaises(ValueError, self.account.withdraw, "5545", 2000, "1122")
