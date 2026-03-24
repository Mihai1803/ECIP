import random

random.seed(42)

transitions = {
    'A': [('B', 0.4), ('C', 0.6)],
    'B': [('A', 0.5), ('B', 0.5)],
    'C': [('A', 0.2), ('B', 0.2), ('C', 0.6)]
}

weights = {
    'A': 1.5,
    'B': 2.0,
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


sequence = ['A']  
for _ in range(15):
    sequence.append(next_state(sequence[-1]))


population = [0.5] 

for state in sequence[1:]:
    r = weights[state]
    p_next = r * population[-1] * (1 - population[-1])
    population.append(p_next)

print("State sequence:")
print(" -> ".join(sequence))

print("\nPopulation values:")
for i in range(len(population)):
    if i == 0:
        print(f"Step {i}: State={sequence[i]}, Population={population[i]:.6f}")
    else:
        print(f"Step {i}: State={sequence[i]}, r={weights[sequence[i]]}, Population={population[i]:.6f}")