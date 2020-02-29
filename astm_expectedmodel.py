# A = 5
# B = [10,15,20]
# B.insert(0,A)
# B.pop(3)
# print(B)
# print(B.index(15))

spares = []
suppliers = ['ABB','SMA','Chint']
for x in suppliers:
    if len(x) < 4:
        spares.append(x)
print(spares)
