# ! python3
# combinePdfs.py - combines all the pdfs in the current working directory into a single PDF

import PyPDF2
import os

# Get all the PDF filenames.
pdfFiles = []

for filename in os.listdir('.'):  # he os.listdir('.') call will return a list of every file in the current working dir.
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()  # A PdfFileWriter object is created to hold the combined PDF pages

for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
