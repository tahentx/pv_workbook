import PyPDF2
import io
import csv

pdfFileObj = open('nrel_sample_agreement.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
text = pageObj.extractText()
s = io.StringIO(text)
with open('terms.csv', 'w') as f:
    for line in s:
        f.write(line)


#
# contract = open('terms.csv','w', newline='')
# terms = csv.writer(contract)
# terms.writerow(['This','is','a','test'])
