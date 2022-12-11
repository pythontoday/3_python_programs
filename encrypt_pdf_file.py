from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass

pdfwriter = PdfFileWriter()
pdf = PdfFileReader('my_pdf.pdf')

for page in range(pdf.numPages):
    pdfwriter.add_page(pdf.pages[page])

password = getpass(prompt='Введите пароль: ')
pdfwriter.encrypt(password)

with open('protected.pdf', 'wb') as file:
    pdfwriter.write(file)
