
def findstring(y):
    z = y.split(' ')
    [z.pop(-1) for i in z if z.count(i) > 1]
    print(z)      
findstring("Boo Boo blam")
