import re


given_text = "cake is 45, 55, 44"

pattern = re.compile('\w+')

result = re.findall(pattern, given_text)
print(result)