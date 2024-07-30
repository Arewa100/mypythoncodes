#peudo code
# 1: create a function called display 
# 2: let the function take in two parameter called a and b
# 3: inside the function, create a variable called product
# 4: write a for loop to calculate the product according to the value of 'a'
# 5: return the result of each iteration



def display(a, b):	
	product = (a, b)
	return product



a = int(input("Enter first value "))
b = int(input("Enter second value "))
	
for counter in range(a + 1):
	result = product(a, b)
	a = a + 1
	b = b + 1
	print(f"{a} {b} {result}")
	


