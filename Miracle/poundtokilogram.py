#peudo code
# 1: create a function called pound_to_kilogram
# 2: let the function take in one parameter called pound
# 3: inside the function, create a variable called pound_in_kilogram
# 4: create a constant variable called ONE_POUND_IN_KILOGRAM and assign its value as 0.454
# 5: multply ONE_POUND_IN_KILOGRAM by the 'pound' and assign its result to the 'pound_in_kilogram'
# 6: return the pound_in_kilogram
# 7: prompt user to enter pound to be converted
# 8: call on function pound_to_kilogram and pass the user input as an argument to it
# 9: assign it result to a declared variable called 'pound_in_kilogram;
# 10: print the result of the converted pound





def pound_to_kilogram(pound):
	ONE_POUND_IN_KILOGRAM = 0.454
	pound_in_kilogram = (pound * ONE_POUND_IN_KILOGRAM)
	
	return pound_in_kilogram


pound = int(input("Enter the pound to be converted:  "))
	
pound_in_kilogram =  pound_to_kilogram(pound)
print(f"the result of {pound} pound in kilogram is {pound_in_kilogram} kilograms")

