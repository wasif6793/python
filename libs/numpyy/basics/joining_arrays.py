import numpy as np

arr1 = np.array([1,2,3,4,5])

arr2 = np.array([1,2,3,4,5])

b = arr1 + arr2
print(b)

arr3 = np.concatenate((arr1, arr2))
print(arr3)