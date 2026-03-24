import numpy as np
import matplotlib.pyplot as plt

r = 0.9
steps = 50

P0_values = [0.1, 0.5, 1, 2, 4]

for P0 in P0_values:
    
    P = np.zeros(steps)
    P[0] = P0

    for t in range(steps - 1):
        P[t+1] = r * P[t] * (1 - P[t])

    plt.figure()
    plt.plot(P, marker='o')
    plt.title(f"Logistic Population Growth (r = 0.9, P0 = {P0})")
    plt.xlabel("Time step")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()