import numpy as np
import matplotlib.pyplot as plt

T = 50
x = np.zeros(T)
x[0] = 0
for t in range(T - 1):
    x[t + 1] = x[t] + 1
t = np.arange(T)

plt.figure()
plt.plot(t, x)
plt.xlabel("Time step t")
plt.ylabel("True state x(t)")
plt.title("Evolution of the True State: x(t+1) = x(t) + 1")
plt.grid(True)
plt.show()