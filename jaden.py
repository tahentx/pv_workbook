def toJadencase(string):
    x = string.split()
    copy = []
    for item in x:
        item = item.title()
        copy.append(item)
    answer = ' '.join(copy)
    print(answer)


toJadencase("bing bam boom")
