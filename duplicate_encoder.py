import collections
word = input("Input word: ")
# creating an empty list & appending the indices to the list makes iteration more manageable. the two lines below do that.
placeholder = []
for x in word:
    placeholder.append(x)


for x in placeholder:
    print(x in placeholder)
