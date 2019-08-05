import numpy as np
from numpy import empty
from numpy import zeros
# Matrix arithmetic, pg. 46, Example 1.17

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
answer = x + y

# Matrix arithmetic, pg. 46, Example 1.18

A = np.array([[2,3],[-1,5]])
x = np.array([2,1])
answer = A * x

# Matrix arithmetic, pg. 51, Example 1.19

f =  np.array([[2,3,6],[1,5,7]])
g =  np.array([[3,7],[4,2],[1,3]])
h = np.matmul(f,g)


a = [5,3,6]
b = [3,9,0]
c = [4,1,1]
d = [a,b,c]

def convert(x,y):
    solution = np.array([x,y])
    print(solution)

def listconvert(z):
    foo = np.array([z])
    determ = np.linalg.det(foo)
    print(foo, determ)

a = empty([3,3])
b = zeros([3,5])
print(b)
