import numpy as np
import matplotlib.pyplot as plt


X = np.random.uniform(0, 1, 10000)

plt.figure()
plt.hist(X, bins=30, edgecolor='black')

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of X ~ Uniform(0,1)")

plt.show()