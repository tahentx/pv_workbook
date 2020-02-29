
import random
researcher = ['Grant','Tina','Emelia','Enrique','Farzad','Vivek','Vijay','Owen','Yolanda','Jackson','Rochelle', 'Renee', 'Krystal','Monica','Abdul','Usama','Lee','Sung']
a = random.choice(researcher)
topic = ['biomedical','forensic accounting','aeronautics','agriculture','clinical psychology','climatology','astronomy','particle physics','marine biology','polymer corrosion', 'voltage imbalance']
b = random.choice(topic)
purpose = ['research grant', 'prototype', 'side project','thesis proposal','dissertation','consulting project']
c = random.choice(purpose)

alpha = .05
result = random.uniform(.02,.08)

def sentence_structure(person, subject, goal):
    print(person + " concluded a " + subject + " study to support a " + goal + ".")

def significance(a,b):
    if a > b:
        print("Reject the null")
    else:
        print("Result not statistically significant.")

sentence_structure(a,b,c)
significance(alpha,result)
