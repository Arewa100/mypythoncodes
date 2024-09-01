from decimal import Decimal
class Account:
    def __init__(self, account_number, firstname, lastname):
        """initialize account object"""
        self.account_number = account_number
        self.firstname = firstname
        self.lastname = lastname
        self.balance = Decimal("0")
        self.pin = "0000"

    def check_balance(self, account_number, pin):
        """method to check the balance of the account"""
        if account_number == self.account_number and pin == self.pin and self.pin != "0000":
            return self.balance
        else:
            raise ValueError("incorrect pin or account_number...")

    def deposit(self, account_number, amount):
        """method to deposit money into the account"""
        if amount > Decimal("0.00") and self.account_number == account_number:
            self.balance = self.balance + Decimal(amount)
        elif not self.account_number == account_number:
            raise ValueError("incorrect account number...")
        elif amount < Decimal("0.00"):
            raise ValueError("invalid amount...")

    def update_pin(self, new_pin):
        """method to update the pin of the account"""
        if new_pin == self.pin or len(new_pin) != 4:
            raise ValueError("ensure pin is 4 digits and not old pin...")
        self.pin = new_pin

    def withdraw(self, account_number, amount, pin):
        """method to withdraw money from the account"""
        if self.account_balance_is_sufficient(amount) and self.pin_is_valid_and_account_number(account_number, pin):
            self.balance = self.balance - Decimal(amount)
        else:
            raise ValueError("incorrect pin, amount or account_number...")

    def account_balance_is_sufficient(self, amount):
        """method to check if the account balance is sufficient"""
        return self.balance >= Decimal(amount) and Decimal(amount) > Decimal('0')

    def pin_is_valid_and_account_number(self, account_number, pin):
        """method to check if the pin is valid and account number"""
        return self.pin == pin and self.account_number == account_number


