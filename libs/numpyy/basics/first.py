import numpy as np

# 1D Array
arr = np.array([1,2,3,4,5])
print(arr)
print("First element: ", arr[0])
print("last element: ", arr[-1])


# 2D Array
arr2 = np.array([[1,2,3,4],[9,8,7,6]])
print(arr2)

print("First element: ", arr2[0][0])
print("last element: ", arr2[-1][-1])

print(arr2[1,-1])
print()


# FInding Dimensions of Array
print(arr.ndim)
print(arr.shape)
print(arr.dtype)
print(arr.itemsize)
print(arr.nbytes)
print()
print(arr2.ndim)