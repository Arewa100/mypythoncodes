def only_floats(firstnumber, secondnumber):
	flagValue = 2.0
	if type(firstnumber) == type(flagValue) and type(secondnumber) == type(flagValue):
		return 2
	elif type(firstnumber) == type(flagValue) or type(secondnumber) == type(flagValue):
		return 1
	else:
		return 0

result = only_floats(7.8, 2.4)
print(result)