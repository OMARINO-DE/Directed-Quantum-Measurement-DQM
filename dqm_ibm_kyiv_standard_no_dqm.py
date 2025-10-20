from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Session
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Load IBM Runtime service and backend
service = QiskitRuntimeService()
backend = service.backend("ibm_kyiv")

# Create standard entangled pair (no DQM rotation)
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Transpile to match backend
qc_transpiled = transpile(qc, backend=backend)

# Run with Sampler and get result
with Session(backend=backend):
    sampler = Sampler()
    job = sampler.run([qc_transpiled])
    result = job.result()

# Extract counts
bitarray = result[0].data["meas"]
counts = bitarray.get_counts()

# Print and plot
print("🧪 Standard measurement counts (no DQM):", counts)
plot_histogram(counts, title="Standard Measurement (No DQM) on Entangled Qubits @ ibm_kyiv")
plt.show()