
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_provider import IBMProvider
from numpy import pi, sin, cos
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Save your IBM Quantum API token (only needed once)
# Get your token from: https://quantum.ibm.com/
# Uncomment the line below and replace 'YOUR_IBM_QUANTUM_TOKEN' with your actual token
# IBMProvider.save_account('YOUR_IBM_QUANTUM_TOKEN', overwrite=True)

# Load IBM account
provider = IBMProvider()

# Get a real backend (e.g., 'ibmq_qasm_simulator' or real quantum device)
backend = provider.get_backend('ibmq_qasm_simulator')

# Directional field function
def directional_field(theta, phi):
    return 0.5 + 0.5 * sin(theta) * cos(phi)

def bias_to_angle(f):
    return 2 * pi * f

# Parameters for DQM (θ and φ in degrees)
theta_deg = 60
phi_deg = 45
theta = theta_deg * pi / 180
phi = phi_deg * pi / 180

# Build DQM circuit
bias = directional_field(theta, phi)
angle = bias_to_angle(bias)

qc = QuantumCircuit(1, 1)
qc.ry(angle, 0)
qc.measure(0, 0)

# Transpile and run
compiled = transpile(qc, backend)
job = backend.run(compiled, shots=1024)
print("Job ID:", job.job_id())

# Get results
result = job.result()
counts = result.get_counts()
print("Measurement Results:", counts)

# Plot
plot_histogram(counts, title=f'DQM on IBM Backend (θ={theta_deg}°, φ={phi_deg}°)')
plt.show()
