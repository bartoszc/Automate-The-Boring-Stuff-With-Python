import PyPDF2
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)  # Here we make a PdfFileReader object of meetingminutes.pdf
minutesFirstPage = pdfReader.getPage(0)  # # We call getPage(0) to get a Page object for the first page
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()  # We make a PdfFileWriter object
pdfWriter.addPage(minutesFirstPage)  # and add the watermarked first page

for pageNum in range(1, pdfReader.numPages):  # we loop through the rest of the pages in meetingminutes.pdf and add them to the PdfFileWriter object
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()
