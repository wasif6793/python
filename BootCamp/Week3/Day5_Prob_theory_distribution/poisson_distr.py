import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

lam = 3
x = np.arange(0,10)
y = poisson.pmf(x,lam)
plt.bar(x,y, color = "blue")
plt.title("Poisson's Distribution")
plt.show()