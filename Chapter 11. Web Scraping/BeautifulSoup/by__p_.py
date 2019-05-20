import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features="html.parser")

pElems = exampleSoup.select('p')
print(str(pElems[0]))
# '<p>Download my <strong>Python</strong> book from <a href="http://inventwithpython.com">my website</a>.</p>'
print(pElems[0].getText())
# 'Download my Python book from my website.'
print(str(pElems[1]))
# '<p class="slogan">Learn Python the easy way!</p>'
print(pElems[1].getText())
# 'Learn Python the easy way!'
print(str(pElems[2]))
# '<p>By <span id="author">Al Sweigart</span></p>'
print(pElems[2].getText())
# 'By Al Sweigart'
