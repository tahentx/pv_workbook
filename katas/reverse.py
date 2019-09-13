def reverse(s):
    x = list(s)
    x.reverse()
    for i in x:
        if isinstance(i,int):
            del i
    y = ''.join(x)
    print(y)
reverse("vibes")
