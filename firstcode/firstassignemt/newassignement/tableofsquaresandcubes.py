print("this is the table of square and cubes")
print("number   square   cube")
for number in range(6):
	square = (number * number)
	cube = (number * number * number)
	print(f"{number:>2}{square:>10}{cube:>10}")