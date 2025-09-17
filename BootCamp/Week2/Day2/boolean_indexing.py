import numpy as np

ar = np.array([1,2,3,4,5,6])
evens =ar[ar%2 == 0]
print("Evens: ",evens)

ar[ar > 3] = 0
print("Modified Array: ",ar)