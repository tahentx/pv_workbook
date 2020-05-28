import itertools
i = itertools.chain.from_iterable(["Ham","sandwich"])
j = [x for x in i]


def off_the_chain(v,b):
    foo = [x for x in itertools.chain(b,v)]
    print(foo)

# off_the_chain("bravo","zulu")

def drop_it(n):
    a = [b for b in itertools.dropwhile(lambda x: x < n,[1,3,5,10,3,4,4,4])]
    print(a) 
# drop_it(10)

def cleanse(a,b):
    x = [y for y in itertools.filterfalse(lambda x: x % a, range(b))]
    print(x)
cleanse(2,10)
