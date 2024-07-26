#peudo code
# 1: create a function called initial_deposit
# 2: let the function take in two parameter called final_account_value and number_of_months
# 3: inside the function, create a constant called ANNUAL RATE
# 4: compute the annual rate and number of years 
# 5: inital deposit amount is calculated as the division of final acoount value and the rate in years
# 6: prompt the user to enter the final amount and years
# 7: print the result





def initial_deposit(final_account_value, number_of_years):
	ANNUAL_RATE = 4.25
	exponent_of_interest_rate = (ANNUAL_RATE ** number_of_years)
	inital_deposit_amount = (final_account_value / exponent_of_interest_rate)
	
	return inital_deposit_amount


final_amount = int(input("Enter the final amount:  "))
years = int(input("Enter the number od years:  "))	
result = initial_deposit(final_amount, years)
print(f"the initial deposit is {result}")

