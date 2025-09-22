import  numpy as np

np.random.seed(45)

a = np.random.rand(3,3)
U, S, Vt = np.linalg.svd(a)

print("MAtrix: \n",a)
print("U: \n", U)
print("Singular Values: \n",S)
print("V transpose: \n", Vt)
