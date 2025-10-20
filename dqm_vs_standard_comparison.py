
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from numpy import pi, sin, cos
import matplotlib.pyplot as plt

# Define DQM directional field function
def directional_field(theta, phi):
    return 0.5 + 0.5 * sin(theta) * cos(phi)

def bias_to_angle(f):
    return 2 * pi * f

# Parameters (theta, phi)
theta = pi / 3
phi = pi / 4
bias = directional_field(theta, phi)
angle_dqm = bias_to_angle(bias)

# Create directed (DQM) circuit
qc_dqm = QuantumCircuit(1, 1)
qc_dqm.ry(angle_dqm, 0)
qc_dqm.measure(0, 0)

# Create standard (non-DQM) circuit
qc_std = QuantumCircuit(1, 1)
qc_std.h(0)  # Hadamard to produce equal superposition
qc_std.measure(0, 0)

# Transpile for simulation
sim = AerSimulator()
compiled_dqm = transpile(qc_dqm, sim)
compiled_std = transpile(qc_std, sim)

# Run simulations
job_dqm = sim.run(compiled_dqm, shots=1024)
job_std = sim.run(compiled_std, shots=1024)
result_dqm = job_dqm.result()
result_std = job_std.result()

# Get measurement counts
counts_dqm = result_dqm.get_counts()
counts_std = result_std.get_counts()

# Plot comparison
plot_histogram([counts_std, counts_dqm], legend=['Standard Measurement', 'Directed (DQM) Measurement'], title='DQM vs Standard Quantum Measurement')
plt.show()
