import re

# match any characyer except for a newine
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))
