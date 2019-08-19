import re

doc = 'nrel_sample_agreement.pdf'
term = re.findall("services",doc)
print(term)
