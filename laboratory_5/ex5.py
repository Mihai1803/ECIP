import numpy as np
import matplotlib.pyplot as plt

A = 1.0
B = 1.0
C = 1.0

Q = 0.01
R = 0.5
P0 = 1.0

T = 50
u = np.ones(T)

np.random.seed(0)

x_true = np.zeros(T)
y = np.zeros(T)

for t in range(1, T):
    w = np.random.normal(0, np.sqrt(Q))
    x_true[t] = A * x_true[t - 1] + B * u[t] + w

for t in range(T):
    v = np.random.normal(0, np.sqrt(R))
    y[t] = C * x_true[t] + v

x_pred_only = np.zeros(T)
x_pred_only[0] = 0.0

for t in range(1, T):
    x_pred_only[t] = A * x_pred_only[t - 1] + B * u[t]

x_kalman = np.zeros(T)
x_kalman[0] = 0.0

P = P0
K_values = np.zeros(T)
P_values = np.zeros(T)

for t in range(1, T):
    x_pred = A * x_kalman[t - 1] + B * u[t]
    P_pred = A * P * A + Q

    K = P_pred * C / (C * P_pred * C + R)

    x_kalman[t] = x_pred + K * (y[t] - C * x_pred)
    P = (1 - K * C) * P_pred

    K_values[t] = K
    P_values[t] = P

mse_pred_only = np.mean((x_true - x_pred_only) ** 2)
mse_kalman = np.mean((x_true - x_kalman) ** 2)

print("MSE (prediction only):", mse_pred_only)
print("MSE (full Kalman filter):", mse_kalman)

plt.figure(figsize=(10, 6))
plt.plot(x_true, label="True state")
plt.plot(y, label="Noisy measurement", linestyle="dotted")
plt.plot(x_pred_only, label="Prediction only", linestyle="--")
plt.plot(x_kalman, label="Kalman estimate", linewidth=2)
plt.xlabel("Time")
plt.ylabel("State")
plt.title("Prediction Only vs Full Kalman Filter")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot((x_true - x_pred_only) ** 2, label="Squared error - prediction only")
plt.plot((x_true - x_kalman) ** 2, label="Squared error - Kalman filter")
plt.xlabel("Time")
plt.ylabel("Squared error")
plt.title("Squared Error Comparison")
plt.legend()
plt.grid()
plt.show()