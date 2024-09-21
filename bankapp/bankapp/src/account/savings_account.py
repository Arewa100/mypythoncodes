from src.account.account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, firstname, lastname, annual_interest_rate):
        super().__init__(account_number, firstname, lastname)
        self.annual_interest_rate = annual_interest_rate

    def modify_interest_rate(self,rate):
        self.annual_interest_rate = rate


    def interest_rate(self):
        return self.annual_interest_rate
