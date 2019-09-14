def reverse(s: str) -> str():
    x = list(s)
    x.reverse()
    if any(isinstance(x,(int)) for i in x):
        x.remove(i)
    y = ''.join(x)
    print(y)
reverse("vib332es")

#
# for i in num:
#     x = isinstance(i, int)
#     if x is True:
#         print(num.index(i))
