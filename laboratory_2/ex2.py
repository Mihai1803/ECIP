import numpy as np
import matplotlib.pyplot as plt


r_values = np.linspace(2.5, 4.0, 2000)   
iterations = 1000
last = 100                              
P0 = 0.5

r_plot = []
P_plot = []

for r in r_values:
    P = P0
    
    for i in range(iterations):
        P = r * P * (1 - P)
        
        if i >= (iterations - last):
            r_plot.append(r)
            P_plot.append(P)

plt.figure(figsize=(10,6))
plt.plot(r_plot, P_plot, ',')
plt.axvline(3.57, linestyle='--', label='Chaos begins (~3.57)')
plt.title("Logistic Map Bifurcation Diagram")
plt.xlabel("Growth factor r")
plt.ylabel("Population")
plt.legend()
plt.show()