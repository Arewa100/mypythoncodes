def milespergallon(miles, gallon):
	quotient = (miles / gallon)
	
	return quotient
gallon = 0
total = 0
counter = 0

while not gallon == -1:
	gallon = float(input("Enter the gallons used(-1 to end): "))
	if not gallon == -1:
		miles = int(input("Enter the miles driven: "))
		result = milespergallon(miles, gallon)
	
		total = total + result
		counter = counter + 1
	
	print(f"the miles/gallon for this tank was {result}")

average = (total / counter)
print(f"The overall average miles/gallon was {average}")