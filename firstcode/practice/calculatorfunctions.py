def add(first_number, second_number):
	return first_number + second_number

def divide(first_number, second_number) -> ZeroDivisionError:
	try:
		return first_number / second_number 
	except ZeroDivisionError:
		raise ZeroDivisionError("Division by zero is not allowed")   
