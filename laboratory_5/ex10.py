import numpy as np
import matplotlib.pyplot as plt

A = 1.0
B = 1.0
C = 1.0

Q = 0.05
R = 0.5
L = 0.5

n_steps = 30

x_true = np.zeros(n_steps)
x_est = np.zeros(n_steps)
y = np.zeros(n_steps)
u = np.zeros(n_steps)
P = np.zeros(n_steps)

x_true[0] = 10.0
x_est[0] = 0.0
P[0] = 1.0

np.random.seed(42)

for t in range(n_steps - 1):
    u[t] = -L * x_est[t]

    w = np.random.normal(0, np.sqrt(Q))
    v = np.random.normal(0, np.sqrt(R))

    x_true[t + 1] = A * x_true[t] + B * u[t] + w
    y[t + 1] = C * x_true[t + 1] + v

    x_pred = A * x_est[t] + B * u[t]
    P_pred = A * P[t] * A + Q

    K = P_pred * C / (C * P_pred * C + R)

    x_est[t + 1] = x_pred + K * (y[t + 1] - C * x_pred)
    P[t + 1] = (1 - K * C) * P_pred

u[-1] = -L * x_est[-1]

time = np.arange(n_steps)

plt.figure(figsize=(10, 5))
plt.plot(time, x_true, label='True state x(t)', marker='o')
plt.plot(time, x_est, label='Estimated state x_hat(t|t)', marker='x')
plt.xlabel('Time step')
plt.ylabel('State')
plt.title('Exercise 10: State and Estimated State')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(time, u, label='Control signal u(t)', marker='o')
plt.xlabel('Time step')
plt.ylabel('Control input')
plt.title('Exercise 10: Control Signal')
plt.legend()
plt.grid(True)
plt.show()