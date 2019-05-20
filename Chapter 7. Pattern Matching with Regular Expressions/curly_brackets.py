import re

# repeat specific number of times
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2 == None)

# returns longes possibility
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo3 = greedyHaRegex.search('HaHaHaHaHa')
print(mo3.group())

# return shortest possibility
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo4 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo4.group())
