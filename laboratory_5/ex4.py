import numpy as np
import matplotlib.pyplot as plt

A = 1.0
B = 1.0
C = 1.0

Q = 0.01
R = 0.5
P = 1.0

T = 50
u = np.ones(T)

np.random.seed(0)

x_true = np.zeros(T)
y = np.zeros(T)

for t in range(1, T):
    process_noise = np.random.normal(0, np.sqrt(Q))
    x_true[t] = A * x_true[t - 1] + B * u[t] + process_noise

for t in range(T):
    measurement_noise = np.random.normal(0, np.sqrt(R))
    y[t] = C * x_true[t] + measurement_noise

x_hat = np.zeros(T)
K_values = np.zeros(T)
P_values = np.zeros(T)

x_hat[0] = 0.0

for t in range(1, T):
    x_pred = A * x_hat[t - 1] + B * u[t]
    P_pred = A * P * A + Q

    K = P_pred * C / (C * P_pred * C + R)

    x_hat[t] = x_pred + K * (y[t] - C * x_pred)
    P = (1 - K * C) * P_pred

    K_values[t] = K
    P_values[t] = P

plt.figure(figsize=(10, 6))
plt.plot(x_true, label='True state')
plt.plot(y, label='Noisy measurement', linestyle='dotted')
plt.plot(x_hat, label='Kalman estimate', linewidth=2)
plt.xlabel('Time')
plt.ylabel('State')
plt.title('Full Kalman Filter')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(K_values, label='Kalman gain K(t)')
plt.xlabel('Time')
plt.ylabel('K(t)')
plt.title('Kalman Gain')
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(P_values, label='Covariance P(t|t)')
plt.xlabel('Time')
plt.ylabel('P(t|t)')
plt.title('Error Covariance')
plt.legend()
plt.grid()
plt.show()