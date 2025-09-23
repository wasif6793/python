import numpy as np

# Simulate Dice rolls and calculate Probabilities

rolls = np.random.randint(1,7, size = 10000)

# Calc Probabilities

P_even = np.sum(rolls % 2 == 0)/ len(rolls)
P_greater_than4 = np.sum(rolls > 4) /len(rolls)
print("P_even: ",P_even)
print("P_greater than 4: ",P_greater_than4)

