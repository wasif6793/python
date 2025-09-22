
import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print("Addition: \n", A + B)

print("Subtraction: \n", A - B)

C = A * 2
print("Multiplication: \n", C)

D = A * B
print("A x B = \n",D)
res = np.dot(A,B)
print("Matrix Multiplication through function: \n", res)

# Identity matrix
I = np.eye(3)
print(I)