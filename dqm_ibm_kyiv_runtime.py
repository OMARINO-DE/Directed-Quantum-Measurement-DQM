from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Session
from qiskit.visualization import plot_histogram
from numpy import pi, sin, cos
import matplotlib.pyplot as plt

# Load IBM Runtime service and backend
service = QiskitRuntimeService()
backend = service.backend("ibm_kyiv")

# Directional Quantum Field
def directional_field(theta, phi):
    return 0.5 + 0.5 * sin(theta) * cos(phi)

def bias_to_angle(f):
    return 2 * pi * f

# Parameters
theta_deg = 60
phi_deg = 45
theta = theta_deg * pi / 180
phi = phi_deg * pi / 180
bias = directional_field(theta, phi)
angle = bias_to_angle(bias)

# Quantum Circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.ry(angle, 0)
qc.measure_all()

# Transpile to match backend
qc_transpiled = transpile(qc, backend=backend)

# Run with Sampler and get result
with Session(backend=backend):
    sampler = Sampler()
    job = sampler.run([qc_transpiled])
    result = job.result()

# Extract measurement BitArray and convert to counts
bitarray = result[0].data["meas"]
counts = bitarray.get_counts()

# Print and plot
print("✅ Final measurement counts:", counts)
plot_histogram(counts, title=f"DQM on Entangled Qubits @ ibm_kyiv (θ={theta_deg}°, φ={phi_deg}°)")
plt.show()