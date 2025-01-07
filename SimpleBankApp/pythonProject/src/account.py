import decimal
from decimal import Decimal


class Account:
    def __init__(self, name:str, account_number: str, password:str):
        self.name = name
        self.account_number = account_number
        self.password = password
        self.balance = Decimal("0")


    def get_balance(self):
        return self.balance

    def deposit(self, account:Decimal):
        if account < decimal.Decimal("0"):
            raise ValueError("Account must be greater than or equal to zero")
        self.balance = self.balance + account

    def withdraw(self, account_number:str, amount:Decimal, password:str):
        if self.balance > amount and account_number == self.account_number and password == self.password:
            self.balance = self.balance - amount