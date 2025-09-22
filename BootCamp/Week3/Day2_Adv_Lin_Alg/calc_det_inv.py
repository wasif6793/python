import numpy as np

np.random.seed(45)
a = np.random.rand(3,3)

print(np.linalg.det(a))
print(np.linalg.inv(a))