word = input("Give a word to flip: ")
foo = word.split()
swap = []
for x in list(foo):
    swap.append(x[::-1])
final = ' '.join(swap)
print(final)
