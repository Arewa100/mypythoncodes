#peudo code
# 1: create a function called total_gravity 
# 2: let the function take in two parameter called subtotal and gravity_rate
# 3: divide gravity_rate by 100 and assign result to a variable called rate
# 4: inside the function, create a variable called gravity
# 5: multply subtotal by the 'rate' and assign its result to the 'gravity'
# 6: create a variable called total
# 7: add subtotal and gravity and assign its result to total
# 8: create a dictionary and name it feedback and assign total and gravity to it as key and value pairs
# 9: return feedback 
# 10: prompt the user to enter subtotal and gravity rate 
# 11: save this values in variables called subtotal and gravity 
# 12: call the function total_gravity and pass the user inputs as argument to it
# 13: assign the results to a variable called feedback
# 14: print the results of the feedback by accessing the elements which is returned as key and value pairs 





def total_gravity(subtotal, gravity_rate):
	rate = (gravity_rate / 100)
	gravity = (subtotal * rate)
	total = (subtotal + gravity)
	feedback = {"gravity": gravity, "total": total}

	return feedback

subtotal = int(input("Enter the subtotal:  "))
gravity_rate = int(input("Enter the gravity rate :  "))

feedback = total_gravity(subtotal, gravity_rate)
print(f"the gravity is {feedback["gravity"]} and total is {feedback["total"]}")

