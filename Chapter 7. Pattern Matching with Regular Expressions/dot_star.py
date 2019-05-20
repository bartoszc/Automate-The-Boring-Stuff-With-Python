import re

# dot character means - any single character except the newline, star character - zero or more of the precending char
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

# nongreedy
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

# greedy
greedyRegex = re.compile(r'<.*>')
mo1 = greedyRegex.search('<To serve man> for dinner.>')
print(mo1.group())
