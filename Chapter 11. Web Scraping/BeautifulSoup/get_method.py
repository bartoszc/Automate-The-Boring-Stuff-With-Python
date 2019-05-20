import bs4
soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
str(spanElem)
# '<span id="author">Al Sweigart</span>'
spanElem.get('id')
# 'author'
print(spanElem.get('some_nonexistent_addr') == None)
# True
print(spanElem.attrs)
# {'id': 'author'}
