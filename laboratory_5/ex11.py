import numpy as np
import matplotlib.pyplot as plt

n_steps = 30

x = np.zeros(n_steps)
u = np.zeros(n_steps)

x[0] = 1.0
u[:] = -0.2

for t in range(n_steps - 1):
    x[t + 1] = x[t] + 0.1 * x[t]**2 + u[t]

time = np.arange(n_steps)

plt.figure(figsize=(10, 5))
plt.plot(time, x, label='State x(t)', marker='o')
plt.plot(time, u, label='Input u(t)', marker='x')
plt.xlabel('Time step')
plt.ylabel('Value')
plt.title('Exercise 11: Nonlinear System')
plt.legend()
plt.grid(True)
plt.show()