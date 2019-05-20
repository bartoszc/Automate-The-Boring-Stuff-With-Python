import re

# will match any vowel, botch lowercase and uppercase
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# will match all the characyers that are ot in the class
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))