import numpy as np
from numpy import empty
from numpy import zeros
from numpy import array
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


a = tuple([5,3,6])
b = tuple([3,9,0])
c = [4,1,1]
d = [a,b,c]

e = zip(a,b)
# print(tuple(e))
# #
# variance = [4,-12,2,3,-3]
# data = array(variance)
# print(data)
# print(type(data))

# create 3 x 3 matrix
delta = [[23,35,63],[22,44,31],[32,5,9]]
bravo = array(delta)
# create features (x) and label (y)
x, y = bravo[:,:-1], bravo[:, -1]

z = np.array([[4,6],[3,9]])
w = np.linalg.det(z)

# khan academy determininant practice problem
E = np.array([[1,5,2],[0,1,4],[-1,0,5]])
det = np.linalg.det(E)



fuse_qty = np.array([85,59])
fuse_cost = np.array([10,50])

value = sum(fuse_cost * fuse_qty)

# union = {2,3,4} | {6,8,0}
# x = {2,8,4} & {6,8,0}
# print(union)
# print(2 in union)
# print(x)
# g = {1,2,3}
# z = {2*i for i in g}
# print(z)

ops = [{'Alpaugh' : 'Diaz','Corcoran' : 'Ellorin','Wisteria' : 'Durazo', 'Panoche' : 'Williams'},{'Alamo': 'Keenan', 'Texas' : 'Ewing'},{'Pilesgrove':'Mattson', 'Penn' : 'Michaels'}]

team = ops[0]
assets = team.keys()
mgrs = team.values()
p = {k:v for (k,v) in team.items() if "P" in k}
print(mgrs)
print(assets)
print(p)
# def convert(x,y):

#     solution = np.array([x,y])
#     print(solution)
#
# def listconvert(z):
#     foo = np.array([z])
#     determ = np.linalg.det(foo)
#     print(foo, determ)
#
# a = empty([3,3])
# b = zeros([3,5])
# print(b)
