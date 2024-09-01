class Account:
    def __init__(self, account_number, firstname, lastname):
        self.account_number = account_number
        self.firstname = firstname
        self.lastname = lastname
        self.balance = 0
        self.pin = "0000"

    def check_balance(self, account_number, pin):
        if account_number == self.account_number and pin == self.pin:
            return self.balance
        else:
            raise ValueError("incorrect pin or account_number...")

    def deposit(self, account_number, amount):
        if amount > 0:
            self.balance = self.balance + amount

    def update_pin(self, new_pin):
        if new_pin == self.pin:
            raise ValueError("pin is same as old pin, enter a unique pin...")
        self.pin = new_pin

