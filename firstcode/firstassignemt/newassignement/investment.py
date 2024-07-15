def investment(amount, years):
	annualrate = 7
	rate_sum = (1 + annualrate)
	rate_exponent_to_years = rate_sum ** years
	
	amount_on_deposit_each_year = (amount * rate_exponent_to_years)
	
	return amount_on_deposit_each_year


amount = int(input("Enter amount on investent: "))

for counter in range(1, 31):
	
	result = investment(amount, counter)
	
	print(f"you have ${result} in year {counter}")
	