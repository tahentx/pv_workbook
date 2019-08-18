
import random
researcher = ['Grant','Emelia','Jackson','Rochelle', 'Renee', 'Krystal','Monica','Abdul','Usama','Lee','Sung']
a = random.choice(researcher)
topic = ['biomedical','forensic accounting','particle physics','marine biology','polymer corrosion', 'voltage imbalance']
b = random.choice(topic)
purpose = ['research grant', 'prototype', 'side project']
c = random.choice(purpose)

def sentence_structure(person, subject, goal):
    print(person + " concluded a " + subject + " study to support a " + goal + ".")

sentence_structure(a,b,c)
