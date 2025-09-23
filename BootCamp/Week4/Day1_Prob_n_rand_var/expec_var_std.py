import numpy as np

# Random variable: Dice roll

outcomes = np.array([1,2,3,4,5,6])
probabilities = np.array([1/6] * 6)
expectation = np.sum(outcomes * probabilities)

print("Expectation: ",expectation)

# Variance
variance = np.sum((outcomes - expectation)**2 * probabilities)
print("Variance: ",variance)

# Std
std = np.sqrt(variance)
print("Std: ",std)
