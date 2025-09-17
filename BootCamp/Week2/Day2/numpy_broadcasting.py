#Broadcasting
# Broadcasting is a powerful NumPy feature that allows you to perform arithmetic operations on
# arrays of different shapes as if they were the same shape — without explicitly copying data.

import numpy as np

ar = np.array([1,2,3])
print(ar + 10)

matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([1,0,1])
print(matrix + vector)

ar2 = np.array([[1,2,3],[4,5,6]])
print("Sum: ",np.sum(ar2))
print("Mean: ", np.mean(ar2))
print("Max:", np.max(ar2))
print("Min:", np.min(ar2))
print("Standard deviation:", np.std(ar2))
print("Sum along rows:", np.sum(ar2, axis=1))
print("Sum along col:", np.sum(ar2, axis = 0))
