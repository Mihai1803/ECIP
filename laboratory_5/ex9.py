import numpy as np
import matplotlib.pyplot as plt

dt = 1.0
n_steps = 30

A = np.array([[1, dt],
              [0, 1]])

C = np.array([[1, 0]])

Q = np.array([[0.01, 0],
              [0, 0.01]])

R = np.array([[1.0]])

x_true = np.zeros((2, n_steps))
y_meas = np.zeros(n_steps)

x_true[:, 0] = np.array([0, 1])

np.random.seed(42)

for t in range(1, n_steps):
    w = np.random.multivariate_normal([0, 0], Q)
    x_true[:, t] = A @ x_true[:, t - 1] + w

for t in range(n_steps):
    v = np.random.normal(0, np.sqrt(R[0, 0]))
    y_meas[t] = (C @ x_true[:, t])[0] + v

x_est = np.zeros((2, n_steps))
P = np.eye(2)

x_est[:, 0] = np.array([0, 0])

for t in range(1, n_steps):
    x_pred = A @ x_est[:, t - 1]
    P_pred = A @ P @ A.T + Q

    y_pred = C @ x_pred
    S = C @ P_pred @ C.T + R
    K = P_pred @ C.T @ np.linalg.inv(S)

    innovation = y_meas[t] - y_pred[0]
    x_est[:, t] = x_pred + (K.flatten() * innovation)
    P = (np.eye(2) - K @ C) @ P_pred

time = np.arange(n_steps)

plt.figure(figsize=(10, 5))
plt.plot(time, x_true[0, :], label='True position', marker='o')
plt.plot(time, x_est[0, :], label='Estimated position', marker='x')
plt.scatter(time, y_meas, label='Measured position', s=25)
plt.xlabel('Time step')
plt.ylabel('Position')
plt.title('True Position vs Estimated Position')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(time, x_true[1, :], label='True velocity', marker='o')
plt.plot(time, x_est[1, :], label='Estimated velocity', marker='x')
plt.xlabel('Time step')
plt.ylabel('Velocity')
plt.title('True Velocity vs Estimated Velocity')
plt.legend()
plt.grid(True)
plt.show()