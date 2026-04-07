import numpy as np
import matplotlib.pyplot as plt


data = np.random.rand(1000)

plt.figure()
plt.hist(data, bins=30, edgecolor='black')

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of 1000 Random Numbers")

plt.show()