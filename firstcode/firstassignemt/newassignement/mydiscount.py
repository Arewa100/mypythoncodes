def mydiscount(price, discount):
	percentage = (discount/100)
	
	percentage_of_price = (percentage * price)
	new_discount_price = (price - percentage_of_price)
	
	return new_discount_price


print("WELCOME TO HILLARY SUPERSTORE")

price = float(input("Enter the price of the goods:  "))
discount = float(input("Enter the discount in percentage: "))
new_price_in_discount = mydiscount(price, discount)
print(f"the new price is {new_price_in_discount}")