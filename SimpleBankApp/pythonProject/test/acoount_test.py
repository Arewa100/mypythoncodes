from unittest import TestCase
from decimal import Decimal

from src.account import Account

class TestForAccount(TestCase):
    the_account:Account = Account("Miracle", "accountNumber", "0000")
    def test_that_account_exists(self):
        self.assertEqual(isinstance(self.the_account, Account), True)

    def test_that_balance_is_zero(self):
        self.assertEqual(self.the_account.get_balance(), Decimal("0"))
    def test_to_deposit_100_balance_is_100(self):
        new_account:Account = Account("Miracle", "accountNumber", "0000")
        new_account.deposit(Decimal("100"))
        self.assertEqual(new_account.get_balance(), Decimal("100"))

    def test_to_deposit_1000_and_500_balance_is_1500(self):
        self.the_account.deposit(Decimal("1000"))
        self.assertEqual(self.the_account.get_balance(), Decimal("1000"))
        self.the_account.deposit(Decimal("100"))
        self.assertEqual(self.the_account.get_balance(), Decimal("1100"))

    def test_to_deposit_a_negative_number_assert_raises_invalid_deposit_number(self):
        self.assertRaises(ValueError, self.the_account.deposit, Decimal("-1000"))

    def test_to_deposit_and_withdraw(self):
        current_account:Account = Account("Miracle", "accountNumber", "password")
        current_account.deposit(Decimal("100"))
        self.assertEqual(current_account.get_balance(), Decimal("100"))
        current_account.withdraw("accountNumber", Decimal("50"), "password")
        self.assertEqual(current_account.get_balance(), Decimal("50"))
