import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(42)

transitions = {
    'A': [('B', 0.4), ('C', 0.6)],
    'B': [('A', 0.5), ('B', 0.5)],
    'C': [('A', 0.2), ('B', 0.2), ('C', 0.6)]
}

weights = {
    'A': 1.5,
    'B': 0.5,   
    'C': 3.3
}

def next_state(current):
    r = random.random()
    cumulative = 0
    for state, prob in transitions[current]:
        cumulative += prob
        if r < cumulative:
            return state
    return transitions[current][-1][0]

steps = 15


states = ['A']
for _ in range(steps):
    states.append(next_state(states[-1]))

P = [0.5]

for i in range(steps):
    r = weights[states[i+1]]
    P_next = r * P[-1] * (1 - P[-1])
    P.append(P_next)

plt.plot(range(len(P)), P, marker='o')
plt.title("Population Evolution (Markov-driven r)")
plt.xlabel("Step")
plt.ylabel("Population")
plt.grid(True)
plt.show()

print("State sequence:")
print(" -> ".join(states))