print("Welcome friend, this a program to print arithmetic sum ,average, product, smallest, largest of three inputs")

def calculator(numberone, numbertwo, numberthree, numberfour):
	sum = (numberone + numbertwo + numberthree + numberfour)
	average = (sum / 3)
	product = (numberone * numbertwo * numberthree * numberfour)
	smallest = min(numberone, numbertwo, numberthree, numberfour)
	largest = max(numberone, numbertwo, numberthree, numberfour)
	
	the_list_of_result = {"sum": sum, "average": average, "product": product, "smallest": smallest, "largest": largest}
	
	return the_list_of_result

def getnumbers():
	first_number = int(input("enter first number: "))
	second_number = int(input("enter second number: "))
	third_number = int(input("enter third number: "))
	fourth_number = int(input("enter fourth number: "))
	
	numbers = {"firstnum": first_number, "secondsum": second_number, "thirdnum": third_number, "fourthnum": fourth_number}
	
	return numbers

for counter in range(10):
	number = getnumbers()

	result = calculator(number["firstnum"], number["secondsum"], number["thirdnum"], number["fourthnum"])

	print(f"the sum is {result["sum"]}")
	print(f"the average is {result["average"]}")
	print(f"the product of the numbers is {result["product"]}")
	print(f"the smallest is {result["smallest"]}")
	print(f"the largest is {result["largest"]} \n" )