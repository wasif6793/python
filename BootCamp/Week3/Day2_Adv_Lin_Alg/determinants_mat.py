import numpy as np

np.random.seed(45)

a = np.random.rand(3,3)

print(np.linalg.det(a))

inverse = np.linalg.inv(a)
print(inverse)
print("\n \n \n \n ")
print(np.linalg.eig(a))
print("\n \n \n \n ")
print(np.linalg.eigvals(a))

