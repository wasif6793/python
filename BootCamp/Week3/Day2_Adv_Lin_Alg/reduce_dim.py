import numpy as np

a = np.random.rand(100,5)

U, S, Vt = np.linalg.svd(a)

k = 2
u_k = U[ : , :k]
s_k = np.diag(S[:k])
V_k = Vt[:k,:]

rand_construct = u_k @ s_k @ V_k

red_data  = u_k @ s_k

print("Approx version: \n",rand_construct)
print()
print("Reduced data: \n",red_data)

