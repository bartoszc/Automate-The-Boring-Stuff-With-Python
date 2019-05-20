import re

# will match everything only up to first newline
noNewLineRegex = re.compile('.*')
print(noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

# will match everything
newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
