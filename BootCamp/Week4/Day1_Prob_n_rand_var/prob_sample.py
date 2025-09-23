from itertools import product

# Sample space of a dice roll
sample_space = list(range(1,7))

#  Probability of rolling and even number
even_number = [2,4,6]
P_even = len(even_number)/len(sample_space)
print("P(Even): ",P_even)