import numpy as np
import matplotlib.pyplot as plt


r = 0.9          
P0 = 0.1         
steps = 50       

P = np.zeros(steps)
P[0] = P0


for t in range(steps - 1):
    P[t+1] = r * P[t] * (1 - P[t])


plt.plot(P, marker='o')
plt.title("Logistic Population Growth Simulation (r = 0.9)")
plt.xlabel("Time step")
plt.ylabel("Population")
plt.grid(True)
plt.show()