
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from numpy import pi, sin, cos
import matplotlib.pyplot as plt

# Directional field function
def directional_field(theta, phi):
    return 0.5 + 0.5 * sin(theta) * cos(phi)

def bias_to_angle(f):
    return 2 * pi * f

# Parameters for DQM
theta = pi / 3
phi = pi / 4
bias = directional_field(theta, phi)
angle = bias_to_angle(bias)

# Create entangled Bell state |Φ+> = (|00> + |11>)/√2
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)

# Apply directional bias only to qubit 0 (as if Alice is encoding)
qc.ry(angle, 0)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Simulate using AerSimulator
sim = AerSimulator()
compiled_circuit = transpile(qc, sim)
job = sim.run(compiled_circuit, shots=1024)
result = job.result()
counts = result.get_counts()

# Plot measurement outcomes
plot_histogram(counts, title='DQM Applied to One Qubit in Entangled Pair')
plt.show()
