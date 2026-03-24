import numpy as np
import matplotlib.pyplot as plt

r_values = [2, 2.5, 1, 1.2, 3.1, 0.5, 4, 4.4, 3, 2.9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]
P0 = 0.1
steps = 50

plt.figure()

for r in r_values:
    P = np.zeros(steps)
    P[0] = P0

    for t in range(steps - 1):
        P[t+1] = r * P[t] * (1 - P[t])

    plt.plot(P, marker='o', label=f"r={r}")

plt.title("Logistic Population Growth for Different r Values")
plt.xlabel("Time step")
plt.ylabel("Population")
plt.grid(True)
plt.legend()

plt.show()
