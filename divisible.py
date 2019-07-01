def isDivisble(n, x, y):
    value = int(n)
    if (value % int(x)) == 0 or value:
        print("Passes test.")
    else:
        print("Logic wrong.")

isDivisble(15,5,13)
