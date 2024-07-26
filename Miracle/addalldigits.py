#peudo code
# 1: create a function called digits_reader
# 2: let the function take in one parameter called digit
# 3: inside the function, create a variable called first, second, third and fourth
# 4: seperate the digit using the floor operator and modulo 
# 5: save result of each seperation into the created variables
# 6: add all variables and save result in a variable called total
# 7: return total 
# 8: prompt the user to enter any digit between 0 and 1000 
# 9: pass the user input as argument to the called function digits_reader
# 10: save result inside a variable called total
# 11: print the result i.e total of the inputed digits


def digits_reader(digit):
	
	first = (digit % 10)
	first_division = (digit // 10)
	second = (first_division % 10) 
	second_division = (first_division // 10)
	third = (second_division % 10) 
	fourth = (second_division // 10)
	
	total = (first + second + third + fourth)
	
	return total


digit = int(input("Enter any digit between 0 and 1000:  "))

total = digits_reader(digit)
print(f"the total of {digit} digits is {total}")

