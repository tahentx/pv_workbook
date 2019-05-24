# https://www.codewars.com/kata/playing-with-digits/train/python
def dig_pow(n,p):
    exp = 1
    x = lambda n,exp : n ** exp
    print(x(n,p))

dig_pow(9,4)
