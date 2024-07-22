def single_filer(taxableincome):
	if taxableincome <= 8350: 
		rate = (10/100)
		tax = (taxableincome * rate)
		
		return tax

	elif taxableincome >= 8351 and taxableincome <= 33950:
		rate = (15/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax

	elif taxableincome >= 33951 and taxableincome <= 82250:
		rate = (25/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax

	elif taxableincome >= 82251 and taxableincome <= 171550:
		rate = (28/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax

	elif taxableincome >= 171551 and taxableincome <= 372950:
		rate = (33/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax
	
	elif taxableincome >= 372951 and taxableincome <= 400000:
		rate = (35/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax


def married_filling_jointly(taxableincome):
	if taxableincome <= 16700: 
		rate = (10/100)
		tax = (taxableincome * rate)
		
		return tax

	elif taxableincome >= 16701 and taxableincome <= 67900:
		rate = (15/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax

	elif taxableincome >= 67901 and taxableincome <= 137050:
		rate = (25/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax

	elif taxableincome >= 137051 and taxableincome <= 208850:
		rate = (28/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax

	elif taxableincome >= 208851 and taxableincome <= 372950:
		rate = (33/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax
	
	elif taxableincome >= 372951 and taxableincome <= 400000:
		rate = (35/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax




def married_filling_seperately(taxableincome):
	if taxableincome <= 8350: 
		rate = (10/100)
		tax = (taxableincome * rate)
		
		return tax

	elif taxableincome >= 8351 and taxableincome <= 33950:
		rate = (15/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax

	elif taxableincome >= 33951 and taxableincome <= 68525:
		rate = (25/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax

	elif taxableincome >= 68525 and taxableincome <= 104425:
		rate = (28/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax

	elif taxableincome >= 104426 and taxableincome <= 186475:
		rate = (33/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax
	
	elif taxableincome >= 186476 and taxableincome <= 400000:
		rate = (35/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax




def head_of_house_hold(taxableincome):
	if taxableincome <= 11950: 
		rate = (10/100)
		tax = (taxableincome * rate)
		
		return tax

	elif taxableincome >= 11950 and taxableincome <= 45500:
		rate = (15/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax

	elif taxableincome >= 45501 and taxableincome <= 117450:
		rate = (25/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax

	elif taxableincome >= 117451 and taxableincome <= 190200:
		rate = (28/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax

	elif taxableincome >= 190201 and taxableincome <= 372950:
		rate = (33/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax
	
	elif taxableincome >= 372951 and taxableincome <= 400000:
		rate = (35/100)
		first_rate = (10/100)
		tax_on_first_rate = (8350 *first_rate)
		result = (taxableincome - 8350)
		feedback = (result * rate)
		tax = (tax_on_first_rate + feedback)
		
		return tax


name = input("Enter your name:  ")
print("Welcome " + name)

flag = ''

while not flag == 'no':
	message = """
	1: press 0 to calculate tax for single filer
	2: press 1 for married filing jointly
	3: prees 2 for married filling seperately
	4: press 3 for head of house
	"""
	print(message)
	
	category = int(input("Select category:  "))
	
	match(category):
		case 0:
			print("welcome to taxable income calculator for single filers")
			taxableincome = int(input("Enter a taxable income:  "))
			feedback = single_filer(taxableincome)
			print(f"Your tax is {feedback}")

		case 1:
			print("welcome to taxable income calculator for married filing jointly")
			taxableincome = int(input("Enter a taxable income:  "))
			feedback = married_filling_jointly(taxableincome)
			print(f"Your tax is {feedback}")

		case 2:
			print("welcome to taxable income calculator for married filling seperately")
			taxableincome = int(input("Enter a taxable income:  "))
			feedback = married_filling_seperately(taxableincome)
			print(f"Your tax is {feedback}")

		case 3:
			print("welcome to taxable income calculator for head of house")
			taxableincome = int(input("Enter a taxable income:  "))
			feedback = head_of_house_hold(taxableincome)
			print(f"Your tax is {feedback}")
		case _:
			print("invalid entry....")


	flag = input("press 'yes' to continue or 'no' to end\n")












