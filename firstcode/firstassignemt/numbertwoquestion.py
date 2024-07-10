#answer to what is wrong with code below

#rating = input('Enter an integer rating between 1 and 10')
#print(type(rating)

#the answer to the above is that the user input is stored as a string rather than an integer. so to solve this i will be using a cast operator to convert the #str datatype of rating to int as written below

rating = int(input('Enter an integer rating between 1 and 10: '))

print(type(rating))