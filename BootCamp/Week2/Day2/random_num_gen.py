import numpy as np

np.random.seed(42)

radnom_array = np.random.rand(3,3)
print("Random Array: ", radnom_array)

random_integers = np.random.randint(0,10, size =(2,3))
print("Random Integers:", random_integers)