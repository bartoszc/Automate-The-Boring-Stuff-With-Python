import re

# re is case-sensitive and includes newlines to match the dot character
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)

someRegexValue1 = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)