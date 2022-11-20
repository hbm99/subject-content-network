# importing required modules
from PyPDF2 import PdfFileReader
from unidecode import unidecode
	
# creating a pdf file object
pdfFileObj = open('Conferencia-00-MN-CC-2021-(con-imagenes).pdf', 'rb')
	
# creating a pdf reader object
pdfReader = PdfFileReader(pdfFileObj, strict = True)
	
# printing number of pages in pdf file
# print(pdfReader.numPages)

text = ""
for i in range(pdfReader.numPages):
    # creating a page object
    pageObj = pdfReader.getPage(i)
        
    # extracting text from page
    text += pageObj.extractText()#.encode('ascii', 'ignore').decode()

# closing the pdf file object
pdfFileObj.close()

print(text)