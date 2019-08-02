import PyPDF2
import pdftables_api
import csv

pdfFileObj = open('ag.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

contract = open('terms.csv','w', newline='')
terms = csv.writer(contract)
terms.writerow(['This','is','a','test'])

c = pdftables_api.Client('yu8wx1021116')
c.csv('nrel_sample_agreement.pdf', 'terms')
