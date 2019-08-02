import PyPDF2
import csv

pdfFileObj = open('ag.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

contract = open('terms.csv','w', newline='')
terms = csv.writer(contract)
terms.writerow(['This','is','a','test'])
