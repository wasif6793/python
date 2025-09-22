from statistics import mode

data = [10,20,30,40,50]
mean = sum(data)/len(data)
print("Mean: ",mean)

# Median
sorted_data = sorted(data)
median = sorted_data[len(data)//2] if len(data)%2 != 0 else \
    (sorted_data[len(data)//2-1]+ sorted_data[len(data)//2])
print("Median:",median)

# Mode
print("Mode: ",mode(data))

# Variance
variance = sum((x-mean)**2 for x in data) / len(data)
print("Variance: ",variance)

# Standard deviation
std = variance **0.5
print("Standard deviation: ",std)