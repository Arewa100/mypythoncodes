#writing dictionaries and nexted dictionaries
#
# students = [{
#     "first_name": "Miracle",
#     "last_name": "Olasoyin",
#     "age": 43,
#     "height": 6.1
# }, {
#     "first_name": "John",
#     "last_name": "Doe",
#     "age": 43,
#     "height": 6.1
# },{
#     "first_name": "Opeyemi",
#     "last_name": "Smith",
#     "age": 43,
#     "height": 6.1
# }]
#
# students[0]["first_name"] = "opeyemi"
# print(students)
#
# NUMBER_OF_STUDENTS = len(students)
# for student in range(NUMBER_OF_STUDENTS):
#     print(students[student]["first_name"])
# # print(students[0]["first_name"])











# family = {
#     "father": "Mr Olu",
#     "mother": "Mrs Olu",
#     "Children": 4,
#     "language": "yoruba"
# }

# for key, value in family.items():
#     #"""this is simply looping through the dictionary"""  this is unpacking
#     print(key, value, end= ' ')

#looping through the keys alone
# for keys in family.keys():
#     print(keys)

# print(family.pop("father"))
# new_family = family.copy()
# print(f"this is the new family copied from 'family'\n{new_family}")
# new_family.clear()
# print(f"this is the new family copied from 'family' after it is  cleared\n{new_family}")
# print(family.get("father", "the key does exists"))
# print(family["father"])


#unpacking iterables

# first_list = range(1, 7)
# #""unpacking it"""
# a, b, *c = first_list
#
# print(a, b, c)

# given_value = [1, 2, 3, 4, 5]
# output = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
from key_multiplier import key_multiplier
given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(key_multiplier(given_list))
