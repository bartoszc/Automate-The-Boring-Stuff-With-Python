import csv
csvFile = open('example.tsv', 'w', newline='')
# delimiter - character between cells - tab
# lineterminator - character between rows - double newline
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
csvFile.close()
