import re

# matches strings that begin with Hello
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!'))
print(beginsWithHello.search('He said hello.'))

# matches strings that end wit a numeric characterfrom 0 to 9
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two'))

# matches strings that both begin and end with one or more numeric characters
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890'))
print(wholeStringIsNum.search('12 34567890'))
