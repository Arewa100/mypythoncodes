from unittest import TestCase

from account import savings_account
from account.savings_account import SavingsAccount


class SavingsAccountTest(TestCase):
    def setUp(self):
        self.savings_account = SavingsAccount("5555", "Olasoyin", "Miracle", 4)
    def test_that_saving_account_exists(self):
        self.assertTrue(isinstance(self.savings_account, SavingsAccount))

    def test_that_savings_account_can_modify_interest_rate(self):
        self.savings_account.modify_interest_rate(4)
        self.assertEqual(self.savings_account.interest_rate(), 4)

    def test_that_savings_account_can_check_balance(self):
       self.savings_account.update_pin("1222")
       self.assertEqual(self.savings_account.check_balance("5555","1222"), 0)

