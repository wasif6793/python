import numpy as np

# Create matrix and vector
A = np.array([[1,2,3],[3,4,4],[4,5,6]])
v = np.array([1,0,-1])

# Matrix- vector multiplication
res = np.dot(A,v)
print(res)

# Diagonal matrix
dm = np.array([[12,0,0],[0,23,0],[0,0,32]])
diag = np.diag([1,4,6])
z = np.zeros((3,3))
print("DIagn=onal: \n",diag)
print("Zero matrix: \n",z)
I = np.eye(3)

inverse = np.linalg.inv(A)
print(inverse)

det = np.linalg.det(A)
print(det)

