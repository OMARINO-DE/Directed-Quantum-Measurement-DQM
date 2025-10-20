
# Directed Quantum Measurement Simulation
# By OMARINO Quantum Labs

import numpy as np
import matplotlib.pyplot as plt

# Create initial quantum state vector
def create_initial_state(alpha, beta):
    norm = np.sqrt(abs(alpha)**2 + abs(beta)**2)
    return np.array([alpha, beta]) / norm

# Directed quantum field function
def directional_field(theta, phi):
    return 0.5 + 0.5 * np.sin(theta) * np.cos(phi)

# Apply DQF bias to quantum state before measurement
def apply_directed_collapse(state, theta, phi):
    f = directional_field(theta, phi)
    directed_state = np.array([
        f * state[0],
        (1 - f) * state[1]
    ])
    norm = np.linalg.norm(directed_state)
    return directed_state / norm if norm != 0 else state

# Quantum measurement simulation
def measure_state(state):
    probabilities = np.abs(state)**2
    return np.random.choice([0, 1], p=probabilities)

# Simulate standard and directed measurements
def simulate_measurements(n, theta, phi):
    alpha, beta = 1, 1
    initial = create_initial_state(alpha, beta)

    directed_results = []
    standard_results = []

    for _ in range(n):
        directed_state = apply_directed_collapse(initial, theta, phi)
        directed_results.append(measure_state(directed_state))
        standard_results.append(measure_state(initial))

    return directed_results, standard_results

# Analyze results
def analyze(results, label):
    zeros = results.count(0)
    ones = results.count(1)
    print(f"{label} - 0: {zeros}, 1: {ones}, Proportion of 1: {ones / len(results):.4f}")

# Run simulation
theta = np.pi / 3
phi = np.pi / 4
num_trials = 1000000

directed, standard = simulate_measurements(num_trials, theta, phi)
analyze(directed, "Directed Measurement")
analyze(standard, "Standard Measurement")

# Plot results
labels = ['0', '1']
counts_directed = [directed.count(0), directed.count(1)]
counts_standard = [standard.count(0), standard.count(1)]

x = np.arange(len(labels))
width = 0.35

plt.bar(x - width/2, counts_standard, width, label='Standard')
plt.bar(x + width/2, counts_directed, width, label='Directed')
plt.xticks(x, labels)
plt.ylabel('Measurement Count')
plt.title('Directed vs Standard Quantum Measurement')
plt.legend()
plt.show()

# Simulate entangled pair under DQF
def entangled_measurement(theta, phi):
    entangled_state = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
    bias = directional_field(theta, phi)
    return np.random.choice(['00', '11'], p=[bias, 1-bias])

# Run entangled simulation
def simulate_entangled(n, theta, phi):
    results = [entangled_measurement(theta, phi) for _ in range(n)]
    count_00 = results.count('00')
    count_11 = results.count('11')
    print(f"Entangled results: 00 = {count_00}, 11 = {count_11}, Proportion of 11 = {count_11/n:.4f}")
    return results

simulate_entangled(10000, theta, phi)
