import re

# optional part
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo3 = phoneNumRegex.search('My number is 415-555-4242.')
print(mo3.group())

mo4 = phoneNumRegex.search('My number is 555-4242.')
print(mo4.group())
