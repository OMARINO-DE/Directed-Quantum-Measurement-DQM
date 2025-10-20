from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from numpy import pi, sin, cos
import matplotlib.pyplot as plt

# Define DQM directional field function
def directional_field(theta, phi):
    return 0.5 + 0.5 * sin(theta) * cos(phi)

# Convert bias to Ry angle
def bias_to_angle(f):
    return 2 * pi * f

# Parameters (theta, phi)
theta = pi / 3
phi = pi / 4
bias = directional_field(theta, phi)
angle = bias_to_angle(bias)

# Build quantum circuit
qc = QuantumCircuit(1, 1)
qc.ry(angle, 0)     # Apply directional bias
qc.measure(0, 0)    # Measure qubit

# Draw the circuit
qc.draw('mpl')
plt.show()

# Use Qiskit AerSimulator
sim = AerSimulator()
compiled_circuit = transpile(qc, sim)
job = sim.run(compiled_circuit, shots=1024)
result = job.result()
counts = result.get_counts()

# Display result
plot_histogram(counts, title='Directed Quantum Measurement Simulation (Qiskit)')
plt.show()
