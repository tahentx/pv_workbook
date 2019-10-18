from sympy import *
import numpy as np
from scipy.stats import hypergeom
x = np.array([2,5])
v_hat = x / (x**2).sum()**0.5
# print(v_hat)
a = np.array([[3,8],[7,5]])
b = np.array([[2,9],[4,2]])
# print(np.matmul(a,b))
[M,n,N] = [6,6,6]
x = hypergeom(M,n,N)

def even_between(lower,upper):
    x = range(lower,upper)
    even_nums = []
    for n in x:
        if n % 2 == 0:
            even_nums.append(n)
        elif n % 2 == 0 or n == upper or n == lower:
            even_nums.append(n)
    print(even_nums)


# even_between(5,19)

def check_anagram(string1,string2):
    rev = string1[::1]
    if rev == string2:
        return True
    else:
        return False

def create_dictionary(lower,upper):
    x = range(lower,upper)
    output = {'even' : [], 'odd' : []}
    for n in x:
        if n % 2 == 0:
            output['even'].append(n)
        else:
            output['odd'].append(n)
    return output
create_dictionary(3,9)
