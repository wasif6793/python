import numpy as np


#Slicing an Array
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[1:6])

print(arr[5:])

print(arr[5:-1])

print(arr[:8: 2])


#Copy an array

x = arr.copy()
print(x)

x[0] = 21
print(x)

# Iterate array using for loop

for i in x:
    print(i, end=' ')

# 2D Array

a2 = np.array([[1,2,3,4],[6,7,8,9]])

for i in a2:
    for j in i:
        print(j, end=' ')

