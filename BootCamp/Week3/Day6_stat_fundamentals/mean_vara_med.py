
import numpy as np

data = [10,30,20,40,50,100]

mean_val = sum(data)/len(data)
print("Mean: ",mean_val)

median_val = np.median(data)
var = np.var(data)
std_dev = np.std(data)

print(f"Mean: {mean_val}, Median: {median_val}, var: {var}, std: {std_dev}")