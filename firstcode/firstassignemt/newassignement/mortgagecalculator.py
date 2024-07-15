def mortgage(amount, duration, rate):
	annualrate = rate/1000
	rate_sum = (1 + annualrate)
	rate_exponent_to_duration = rate_sum ** duration
	
	rate_calculated_numberator = (rate * rate_exponent_to_duration)
	rate_calculated_denominator = (rate_exponent_to_duration - 1)
	rate_division = (rate_calculated_numberator / rate_calculated_denominator)
	
	monthly_payment = (amount * rate_division)
	
	
	return monthly_payment 

for counter in range(10):
	
	amount = int(input("Enter amount on investent:  "))
	rate = int(input("Enter the annual interest rate:  "))
	duration = int(input("Enter the duration in years:  "))
	
	result = mortgage(amount, duration, rate)
	
	print(f"your monthly payment is ${result}")
	