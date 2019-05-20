import os
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

for file in os.listdir('/home/bart/PycharmProjects/Python_Main/Automate the Boring Stuff/Project: Regex Search'):
    with open(file, 'r') as open_file:
        all_text = open_file.read()
    print(phoneNumRegex.findall(all_text))






