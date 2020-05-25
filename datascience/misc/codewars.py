import itertools
i = itertools.chain.from_iterable(["Ham","sandwich"])
j = [x for x in i]


def off_the_chain(v,b):
    foo = [x for x in itertools.chain(b,v)]
    print(foo)

off_the_chain("bravo","zulu")
