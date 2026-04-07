import numpy as np
import matplotlib.pyplot as plt

x = 10
noise = np.random.normal(0, 1, 10000)
y = x + noise
estimate = np.mean(y)

print("Estimated value:", estimate)
print("True value:", x)
print("Estimation error:", estimate - x)
