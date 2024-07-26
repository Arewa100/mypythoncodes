#peudo code
# 1: create a function called feet_to_meters
# 2: let the function take in one parameter called feet
# 3: inside the function, create a variable called feet_in_meters
# 4: create a constant variable called ONE_FOOT_IN_METERS and assign its value as 0.305
# 5: multply ONE_FOOT_IN_METERS by the 'feet' and assign its result to the 'feet_in_meters'
# 6: return the feet_in_meters
# 7: prompt user to enter feet to be converted
# 8: call on function feet_to_meters and pass the user input as an argument to it
# 9: assign it result to a declared variable called 'feet_in_meters
# 10: print the result of the converted feet


def feet_to_meters(feet):
	ONE_FOOT_IN_METERS = 0.305
	feet_in_meters = (feet * ONE_FOOT_IN_METERS)
	
	return feet_in_meters


feet = int(input("Enter the feet to be converted:  "))
	
feet_in_meters =  feet_to_meters(feet)
print(f"the result of {feet} feet in meters is {feet_in_meters} meters")