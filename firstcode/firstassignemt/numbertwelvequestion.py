print("welcome friend")
principal = int(input("Enter the original amount invested: "))
annual_return_rate = int(input("Enter the annual return rate: "))
number_of_years = int(input("Enter the number of years: " ))

rate_increment = (1 + annual_return_rate)
rate_to_number_years = (rate_increment ** number_of_years)

amount_on_deposite = (principal * rate_to_number_years)

print("the amount on deposite at the end of the nth year is", amount_on_deposite)