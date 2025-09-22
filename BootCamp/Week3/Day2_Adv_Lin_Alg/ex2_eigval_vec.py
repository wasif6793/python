import numpy as np

np.random.seed(45)
a = np.array([[3,1,1],[-1,3,1],[1,1,3]])

print("Original matrix: \n",a)

# eigval, eigvec = np.linalg.eigvals(a)
#
# print("Eigen values \n",eigval)
# print("\n")
# print("Eigen vectors: \n", eigvec)

# SVD

U, S, Vt = np.linalg.svd(a)

print("S: \n",S)
print("U \n", U)
print("Vt: \n", Vt)


# Reconstruct
sigma = np.zeros((3,3))
np.fill_diagonal(sigma,S)
recons = U @ sigma @ Vt
print("Reconstruct: \n",recons)
