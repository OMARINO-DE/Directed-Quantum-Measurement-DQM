
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_provider import IBMProvider
from numpy import pi, sin, cos
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Save your IBM Quantum API token (only needed once)
# Get your token from: https://quantum.ibm.com/
# Uncomment the line below and replace 'YOUR_IBM_QUANTUM_TOKEN' with your actual token
# IBMProvider.save_account('YOUR_IBM_QUANTUM_TOKEN', overwrite=True)

# 1. Load IBM Quantum account (token must be saved previously using IBMProvider.save_account())
provider = IBMProvider()

# 2. Select backend
backend = provider.get_backend("ibm_kyiv")  # or 'ibmq_manila' for real device

# 3. Directional Quantum Field function
def directional_field(theta, phi):
    return 0.5 + 0.5 * sin(theta) * cos(phi)

def bias_to_angle(f):
    return 2 * pi * f

# 4. DQM parameters
theta_deg = 60
phi_deg = 45
theta = theta_deg * pi / 180
phi = phi_deg * pi / 180
bias = directional_field(theta, phi)
angle = bias_to_angle(bias)

# 5. Create entangled state |Φ+> = (|00> + |11>)/√2
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)

# 6. Apply DQM bias to qubit 0 (Alice)
qc.ry(angle, 0)

# 7. Measure both qubits
qc.measure([0, 1], [0, 1])

# 8. Transpile and run on backend
compiled = transpile(qc, backend)
job = backend.run(compiled, shots=1024)
print("Job ID:", job.job_id())

# 9. Retrieve and visualize results
result = job.result()
counts = result.get_counts()
print("Measurement Results:", counts)
plot_histogram(counts, title=f"DQM on Entangled Qubits (θ={theta_deg}°, φ={phi_deg}°)")
plt.show()
