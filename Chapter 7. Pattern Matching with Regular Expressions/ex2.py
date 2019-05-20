""" How would you write a regex that matches the full name of someone whose last name is Nakamoto? You can assume that
    the first name that comes before it will always be one word that begins with a capital letter. The regex must match
    the following:

    'Satoshi Nakamoto'
    'Alice Nakamoto'
    'Robocop Nakamoto'

    but not the following:

    'satoshi Nakamoto' (where the first name is not capitalized)
    'Mr. Nakamoto' (where the preceding word has a nonletter character)
    'Nakamoto' (which has no first name)
    'Satoshi nakamoto' (where Nakamoto is not capitalized)"""

import re
re.compile(r'[A-Z][a-z]*\sNakamoto')