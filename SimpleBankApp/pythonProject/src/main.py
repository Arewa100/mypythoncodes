import numpy as np
import random
from decimal import Decimal

import re

# created_array = np.array([[2, 4, 4], [3, 7, 9]])
#
#
#
# print(created_array[0][1])
#
#
# result = np.array([count for count in range(2, 20, 2)])
#
# print(result)
# print(result.dtype)
# print(result.shape)
# print(result.size)
# print(result.itemsize)

# two_dimensional = np.array([[even for even in range(2, 10, 2)], [odd for odd in range(1, 10, 2)]])
#
# print(two_dimensional

# two_dimensional = np.array([[1, 3, 4, 5], [2, 4, 5, 3]])
#
# for row in two_dimensional:
#     for column in row:
#         print(column, end=' ')
# x = 0


# result = np.linspace(0., 1, num=5)
# print(result)

#
# the_value= random.randrange(1, 7)
# print(the_value)


# generate_array = np.array([2, 4, 5, 6])
# print(f"{generate_array >= 4}") #this creates a boolean type of result


#experimenting with deep copies
# first_array = np.arange(1, 7).reshape(2, 3)
# print(first_array.sum())
# second_array = first_array.copy()
# print(second_array)
#
#
#
# first_array *= 2
#
# print(first_array)
# print(second_array)
#
#
# square_root_them = np.sqrt(first_array)
#
# print(square_root_them)

# first = np.array([1, 2, 3])
# second = np.array([4, 5, 6])
#
# print(np.add(first, second))
#
# print(np.multiply(first, [3, 1, 2])) #this is broadcasting
#
# tw_d = np.arange(1, 7).reshape(2, 3)
# print(tw_d[0, 1])

# print(f"{12.22:.1f}")
# age = int(input("what is your age: "))
#
# print(f"you are {age} years old")

# print(f"{23:c}")
# print(f"{Decimal("120000000000000.00"):.1e}")
# print(f'{58:c}{45:c}{41:c}')
# print(f"[{12.3:10f}]")
#
# text = "i lov you eri okan me"
# print(f"{text.count("eri, 12")}")
#
# if "oraNge" == "oraNge":
#     print("true")
# else:
#     print("false")
#
#
# print(f"{"love" not in text}")
#
# if text.startswith("i"):
#     print("true")
#
#
# #testing out raw string
#
# print(r'c:\desktop\python')


# pattern = '12222'
#
# userinput = input("enter any text to match the given pattern: ")
#
# result = re.fullmatch(pattern, userinput)
#
# print(result)

# result = 'Valid' if re.fullmatch(r'\w{5}', 'A_AAA') else "Invalid"
#
# print(result)

# name = input("Enter your name: ")
#
# if re.fullmatch(r'[A-Z][a-z]*', name):
#     print("name pattern is valid")
# else:
#     print("name pattern is invalid")

# checking = 'valid' if re.fullmatch('[^a-z]', 'A') else 'invalid'
# second_check = 'valid' if re.fullmatch('[*&#@]', '?') else 'invalid'
# third_check = 'valid' if re.fullmatch('gree?dy', 'greeedy') else 'invalid'
# fourth_check = 'valid' if re.fullmatch(r'\d{3,}', '113333') else 'invalid'
#
# fifth_check = 'valid' if re.fullmatch(r'\d{3,4}', '1133') else 'invalid'
# print(fifth_check)

# test_regex = 'Street is valid' if re.fullmatch(r'\d+ [A-Z][a-z]* [A-Z][a-z]*', '123 Main Street') else 'Street is invalid'
# print(test_regex)'


testing_replacement = re.sub(r'\t+ ',',', 'A\tB\t\tC\t\t\tD' )

print(testing_replacement)