# ! python3
# breaker.py - program that will decrypt the PDF by trying every possible English word until it finds one that work

import PyPDF2


def pass_breaker(txt_file, pdf_file):
    with open(txt_file) as f:
        content = f.read().splitlines()

    new_content = [word.lower() for word in content] + content
    for index, word in enumerate(new_content):
        if pdf_file.decrypt(word):
            print(f'Correct! Password: {word}')
            break
        else:
            print(index)
            continue


file = PyPDF2.PdfFileReader(open('Numpy_encrypted.pdf', 'rb'))
print(pass_breaker('dictionary.txt', file))