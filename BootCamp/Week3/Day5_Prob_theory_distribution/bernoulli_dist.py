import numpy as np
import  matplotlib.pyplot as plt

p = 0.6
plt.bar([0,1],[1-p,p],color = "blue")
plt.title("Bernoulli distribution")
plt.xticks([0,1],labels=["0 (failure)","1 (Success)"])
plt.show()