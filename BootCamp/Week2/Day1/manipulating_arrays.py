import numpy as np
from numpy.ma.core import reshape

arr = np.array([1,2,3,4,5,6,7,8,9])
reshaped = arr.reshape((3,3))
print(arr)
print(reshaped)

expanded = arr[:,np.newaxis]
print(expanded)

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a + b)
print( a * b)
print( a / b)
print(a // b)

#Mathematical operations
a2 = np.array([1,2,3])
print(np.sqrt(a2))
print(np.max(a))
print(np.sum(a2))
print(np.square(a2))