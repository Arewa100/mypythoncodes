print("welcome to the multiplication table")
number = int(input("Enter a number to view it multiplication table:  "))

for counter in range(1, 11): 
	result = (number * counter) 
	print(f"{number} x {counter} = {result}")