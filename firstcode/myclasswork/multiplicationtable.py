print("WELCOME TO AREWA MULTIPLICATION TABLE")

def multiply(number, count):
	result = number * count
	
	return result


number1 = 1
number2 = 2
number3 = 3
number4 = 4
number5 = 5
number6 = 6
number7 = 7
number8 = 8
number9 = 9
number10 = 10
number11 = 11
number12 = 12


for count in range(1, 13):
	result1 = multiply(number1, count)
	result2 = multiply(number2, count)
	result3 = multiply(number3, count)
	result4 = multiply(number4, count)
	result5 = multiply(number5, count)
	result6 = multiply(number6, count)
		
	print(f"{number1} x {count} = {result1:<8} {number2} x {count} = {result2:<8} {number3} x {count} = {result3:<8} {number4} x {count} = {result4:<8}  {number5} x {count} = {result5:<8} {number6} x {count} = {result6:<8}")
	

for count in range(1, 13):

	result7 = multiply(number7, count)
	result8 = multiply(number8, count)
	result9 = multiply(number9, count)
	result10 = multiply(number10, count)
	result11 = multiply(number11, count)
	result12 = multiply(number12, count)
	
	
	print(f"{number7} x {count} = {result7:<8} {number8} x {count} = {result8:<9} {number9} x {count} = {result9:<8} {number10} x {count} = {result10:<8} {number11} x {count} = {result11:<8} {number12} x {count} = {result12:<8}")








