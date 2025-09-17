import numpy as np

ar = np.array([[1,2,3],[4,5,6],[7,8,9]])
vec = np.array([1,0,-1])
res = ar + vec
print("add:", res)

res_mul = ar * 2
print("Mul:", res_mul)
