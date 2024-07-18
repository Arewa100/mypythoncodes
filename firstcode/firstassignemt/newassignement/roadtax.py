def roadtax(carcost):

	if carcost < 1000000:
		car_roadtax = taxcalculator(carcost, 10)
		
		return car_roadtax
	elif carcost < 3000000:
		car_roadtax = taxcalculator(carcost, 15)
		
		return car_roadtax
	elif carcost < 5000000:
		car_roadtax = taxcalculator(carcost, 20)
		return car_roadtax
	else:
		car_roadtax = taxcalculator(carcost, 25)
		return car_roadtax

def taxcalculator(cost, percentage):
	percentageCost = (percentage/100)
	calculated_tax = (cost * percentageCost)
	
	return calculated_tax

car_type = input("What is the name of your car: ")

flag = ''
while flag  != "no":
	carcost = int(input("Enter the cost of your car:  "))
	amount_paid_on_road_tax = roadtax(carcost)
	
	print(f"the road tax to be paid based on your {car_type} car price is {amount_paid_on_road_tax}")
	
	flag = input("press yes to continue or no to end:  ")
	








