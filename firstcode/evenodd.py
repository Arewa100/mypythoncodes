print("welcome to my even and odd number calculator")
number = input("enter a number: ")

number = int(number)

print(type(number))

result = (number % 2)
if(result == 0):
	print(number ," is even")
else:
	print(number, "is a odd number")