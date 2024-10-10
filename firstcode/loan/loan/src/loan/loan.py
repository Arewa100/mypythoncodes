class Loan:
    def __init__(self, firstname, lastname, annual_interest_rate, loan_amount, duration_of_loan):
        self.__name = f"{firstname} {lastname}"
        self.annual_rate = annual_interest_rate
        self.loan_amount = loan_amount
        self.loan_duration = duration_of_loan

    @property
    def name(self):
        return self.__name

    @property
    def annual_rate(self):
        return self.__annual_rate

    @annual_rate.setter
    def annual_rate(self, rate):
        if self.__is_above_zero(rate):
            self.__annual_rate = rate
        else:
            raise ValueError("rate cannot be negative")


    @property
    def loan_amount(self):
        return self.__loan_amount

    @loan_amount.setter
    def loan_amount(self, amount):
        if self.__is_above_zero(amount):
            self.__loan_amount = amount
        else:
            raise ValueError("Loan amount cannot be negative")

    def __is_above_zero(self, value):
        return True if value > 0 else False

    @property
    def loan_duration(self):
        return self.__loan_duration

    @loan_duration.setter
    def loan_duration(self, value):
        if self.__is_above_zero(value):
            self.__loan_duration = value
        else: raise ValueError("Loan duration cannot be negative")

    def compute_monthly_payment(self):
        numerator = self.loan_amount *  self.annual_rate
        monthly_interest_rate = 1/(1 + self.annual_rate)
        new_result = monthly_interest_rate**self.loan_duration
        return numerator / new_result

    def total_payment(self):
        monthly_payment = self.compute_monthly_payment()
        return monthly_payment ** self.loan_duration

