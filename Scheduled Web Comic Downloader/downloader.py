#! python3
# downloadXkcd.py - Downloads comic with cron - schedule tool

import requests
import os
import bs4

url = 'http://www.lefthandedtoons.com'
print('Downloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features='html.parser')

# Find the URL of the comic image.
comicElem = soup.select('.comicimage')
if not comicElem:
    print('Could not find comic image.')
else:
    comicURL = comicElem[0].get('src')
    # Download the image.
    print('Downloading image %s...' % comicURL)
    res = requests.get(comicURL)
    res.raise_for_status()

    # Save the image to ./xkcd.
    imageFile = open(os.path.join('/home/bart/Desktop', os.path.basename(comicURL)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()


print('Done.')
