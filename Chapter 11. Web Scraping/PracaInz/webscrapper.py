import requests
import bs4
import os

with open('source_list.txt') as open_f:
    pages = open_f.read()

for page in pages:
    print('Downloading page %s...' % page)
    res = requests.get(page)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features='html.parser')

