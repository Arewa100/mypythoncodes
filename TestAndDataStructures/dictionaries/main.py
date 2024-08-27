# #writing dictionaries and nexted dictionaries
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


family = {
    "father": "Mr Olu",
    "mother": "Mrs Olu",
    "Childen": 4,
    "language": "yoruba"
}
#
# print(family.pop("father"))
new_family = family.copy()
print(f"this is the new family copied from 'family'\n{new_family}")
print(family.get("father", "the key does exists"))
print(family["father"])
