import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)

print(exampleData[0][0])
# '4/5/2015 13:34'
print(exampleData[0][1])
# 'Apples'
print(exampleData[0][2])
# '73'
print(exampleData[1][1])
# 'Cherries'
print(exampleData[6][1])
# 'Strawberries'
