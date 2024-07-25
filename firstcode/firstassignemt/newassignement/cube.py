def cube(x):
	"""Calculate the cube of x."""
	x ** 3
print('The cube of 2 is', cube(2))



#the above function does not have a return statement so its returning false
#correction version
def cube(x):
	"""Calculate the cube of x."""
	result = x ** 3
	return result
	
print('The cube of 2 is', cube(2))