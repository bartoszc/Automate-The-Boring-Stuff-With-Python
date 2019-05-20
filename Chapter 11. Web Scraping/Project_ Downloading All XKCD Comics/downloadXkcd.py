#! python3
# downloadXkcd.py - Downloads every single XCD comic.

import requests
import os
import bs4

url = 'http://xkcd.com'                 # starting url
os.makedirs('xkcd', exist_ok=True)      # store comics in ./xkcd. exist_ok=True keyword argument prevents the function
                                        # from throwing an exception if this folder already exists.

while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features='html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if not comicElem:
        print('Could not find comic image.')
    else:
        comicURL = comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % comicURL)
        res = requests.get(comicURL)
        res.raise_for_status()

        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the prev buttons url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')