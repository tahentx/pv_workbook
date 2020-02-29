def find_it(seq: list) -> int:
    for x in seq:
        if seq.count(x) % 2 == 0:
            pass
        else:
            return x

find_it([1,1,3])
