#peudo code
# 1: create a function called area_of_cylinder
# 2: let the function take in one parameter called radius
# 3: inside the function, create a variable called area
# 4: create a constant variable called PI and assign its value as 3.142
# 5: multply Pi by the square of the radius and assign its result to the area
# 6: return the area


# 7: create a function called volume_of_cylinder
# 8: let the function take in two parameter called area and length
# 9: inside the function, create a variable called volume
# 10: multply area by the length and assign its result to the volume
# 11: return volume

#12: prompt user to enter radius and save entry inside a variable called radius
#13: call the area function and pass the user entry to the parameter of the function
#14: create a variable called area and assign it to the function area_of_cylinder
#15: print the area of the cylinder
#16: call the volume funcntion and pass the calculated area to the paramter of the function and length
#17: assign its result to a variable called volume and
#18: print the result in the terminal
#19: i will be printing the result on the same line


def area_of_cylinder(radius):
	PI = 3.142
	product_of_radius = (radius * radius)
	area = (PI * product_of_radius)
		
	return area

def volume_of_cylinder(area, length):

	product_of_inputs = (area * length)
	volume = product_of_inputs
		
	return volume

radius = int(input("Enter the radius of a cylinder:  "))
length = int(input("Enter the length of a cylinder:  "))

area = area_of_cylinder(radius)
volume = volume_of_cylinder(area, length)

print(f"the area of the cylinder is {area}, and volume is {volume}") 

