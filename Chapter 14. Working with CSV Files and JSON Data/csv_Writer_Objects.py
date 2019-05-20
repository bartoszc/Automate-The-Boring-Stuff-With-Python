import csv
outputFile = open('output.csv', 'w', newline='')  # call open() and pass it 'w' to open a file in write mode
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])  # 21
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])  # 32
outputWriter.writerow([1, 2, 3.141592, 4])  # 16 - number of characters written to the file for that row
outputFile.close()
