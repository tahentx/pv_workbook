def duplicate(word):
    word2 = list(word)
    word3 = []
    for x in word2:
        word3.append(x)
        if word2.count(x) > 1:
            word3.append(x)
    print(word3)
duplicate("Hell")
