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
        if amount > 0 and self.account_number == account_number:
            self.balance = self.balance + Decimal(amount)
        elif not self.account_number == account_number:
            raise ValueError("incorrect account number...")
        elif amount < 0:
            raise ValueError("invalid amount...")

    def update_pin(self, new_pin):
        """method to update the pin of the account"""
        if new_pin == self.pin or len(new_pin) != 4:
            raise ValueError("ensure pin is 4 digits and not old pin...")
        self.pin = new_pin


