import numpy as np

#ar = np.array([[1,2,3,4,5][4,5,6,7,8],[6,7,8,9,10],[9,10,11,12,13],[12,13,14,15,16]])

randd = np.random.randint(1,51,size=(5,5))
print("Original: \n",randd)

print("Sum original: ",np.sum(randd))

#Filter values > 25 and replaced with 0
randd[randd >25] = 0
print("Modified dataset", randd)

#calculte summary stats
print("Sum:", np.sum(randd))
print("Mean:", np.mean(randd))
print("Standard deviation:",np.std(randd))
