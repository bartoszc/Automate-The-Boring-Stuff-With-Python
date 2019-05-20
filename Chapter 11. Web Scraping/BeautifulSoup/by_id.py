import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features="html.parser")
elems = exampleSoup.select('#author')
print(type(elems))
# <class 'list'>
print(len(elems))
# 1
print(type(elems[0]))
# <class 'bs4.element.Tag'>
print(elems[0].getText())
# 'Al Sweigart'
print(str(elems[0]))
# '<span id="author">Al Sweigart</span>'
print(elems[0].attrs)
# {'id': 'author'}
