import numpy as np

input = np.array([[2,-1],[4,3]])
w, v = np.linalg.eig(input)
print(w,v)
