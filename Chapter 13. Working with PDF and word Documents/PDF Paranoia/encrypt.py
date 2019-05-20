# ! python3
# encrypt.pdf - encrypt the PDFs in folder using a password provided on the command line

import PyPDF2
from PyPDF2 import utils
import os
import sys


def encrypt_pdf(passw):

    for foldernames, subfolders, filenames in os.walk('/home/bart/PycharmProjects/Python_Main/'
                                                      'Automate the Boring Stuff/'
                                                      'Chapter 13. ''Working with PDF and word Documents/PDF Paranoia'):
        for filename in filenames:
            if filename.endswith('.pdf'):
                pdf_file = open(filename, 'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                try:
                    pdf_reader.getPage(0)
                    pdf_writer = PyPDF2.PdfFileWriter()
                    for pageNum in range(pdf_reader.numPages):
                        pdf_writer.addPage(pdf_reader.getPage(pageNum))
                    pdf_writer.encrypt(passw)
                    new_name = filename[:-4] + '_encrypted.pdf'
                    result_pdf = open(new_name, 'wb')
                    pdf_writer.write(result_pdf)
                    result_pdf.close()
                    pdf_reader = PyPDF2.PdfFileReader(open(new_name, 'rb'))
                    try:
                        pdf_reader.decrypt(password)
                        os.unlink(filename)
                    except PyPDF2.utils.PdfReadError:
                        print(f'Error: The file {new_name} is not encrypted')
                except PyPDF2.utils.PdfReadError:
                    print(f'{filename} is already encrypted!')
                    continue


def decrypt_pdf():
    for foldernames, subfolders, filenames in os.walk('/home/bart/PycharmProjects/Python_Main/'
                                                      'Automate the Boring Stuff/'
                                                      'Chapter 13. ''Working with PDF and word Documents/PDF Paranoia'):
        for filename in filenames:
            if filename.endswith('.pdf'):
                print(f'I found a file: {filename}')
                password = input('Enter a password to decrypt the file: ')
                try:
                    pdf_reader = PyPDF2.PdfFileReader(open(filename, 'rb'))
                    pdf_reader.decrypt(password)
                    pdf_writer = PyPDF2.PdfFileWriter()
                    for pageNum in range(pdf_reader.numPages):
                        pdf_writer.addPage(pdf_reader.getPage(pageNum))
                    new_name = filename[:-4] + '_decrypted.pdf'
                    result_pdf = open(new_name, 'wb')
                    pdf_writer.write(result_pdf)
                    print('Done')
                    result_pdf.close()
                except PyPDF2.utils.PdfReadError:
                    print("Wrong password")
                    continue


if len(sys.argv) < 2:
    print('Password was not provided!')
    exit(0)
else:
    password = sys.argv[1]
    print('Encrypt or decrypt? ')
    choice = input()
    if choice.lower() == 'encrypt':
        encrypt_pdf(password)
    elif choice.lower() == 'decrypt':
        decrypt_pdf()
    else:
        print('Unknown command')
