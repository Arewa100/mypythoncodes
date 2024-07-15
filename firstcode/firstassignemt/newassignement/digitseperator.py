def digitseperator(number): 

	first_division = (number // 10);  
	first_index = (number % 10); 

	second_division = (first_division // 10); 
	second_index = (first_division % 10);  

	third_division = (second_division // 10); 
	third_Index = (second_division % 10); 

	fourth_division = (third_division // 10); 
	fourth_index = (third_division % 10); 
		
	fifth_index = fourth_division;
	
	seperated_digit = {"first": fifth_index, "second": fourth_index, "third": third_Index, "fourth": second_index, "fifth": first_index}
	
	return seperated_digit

while(True):
	number = int(input("Enter any five digit: "))
	result = digitseperator(number)
	print(result["first"])
	print(result["second"])
	print(result["third"])
	print(result["fourth"])
	print(result["fifth"])