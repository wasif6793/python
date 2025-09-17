import numpy as np
np.random.seed(42)
ar = np.random.randint(1,50,size = (3,3))
print("Array:",ar)
print(np.sum(ar.sum(axis = 0)))