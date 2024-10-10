from unittest import TestCase
from src.loan.loan import Loan
class TestLoan(TestCase):
    def setUp(self):
        self.loan: Loan = Loan("Grady", "Boosh", 12, 2000, 1)

    def test_that_loan_exists(self):
        self.assertEqual(isinstance(self.loan, Loan), True)

    def test_that_borrower_name_has_been_initialised(self):
        self.assertEqual(self.loan.name, "Grady Boosh")

    def test_that_annual_interest_rate_has_been_initialised(self):
        self.assertEqual(self.loan.annual_rate, 12)

    def test_that_loan_amount_has_been_set(self):
        self.assertEqual(self.loan.loan_amount, 2000)

    def test_that_duration_of_loan_has_been_set(self):
        self.assertEqual(self.loan.loan_duration, 1)

    def test_that_loan_amount_can_not_be_set_to_negative(self):
        self.assertRaises(ValueError, Loan, "Grady", "Boosh", 12, -2000, 1)

    def test_that_interest_rate_cannot_be_set_to_negative(self):
        self.assertRaises(ValueError, Loan, "Grady", "Boosh", -12, 2000, 1)

    def test_that_year_can_not_be_set_to_zero(self):
        self.assertRaises(ValueError, Loan, "Grady", "Boosh", 12, 2000, 0)

    def test_that_monthly_payment_on_loan_can_be_gotten(self):
        self.assertEqual(self.loan.compute_monthly_payment(), 4000)

    def test_to_check_total_payment(self):
        self.assertEqual(self.loan.total_payment(), 4000)

