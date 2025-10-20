import tkinter as tk
from tkinter import ttk
from numpy import pi, sin, cos
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# DQM directional field function
def directional_field(theta, phi):
    return 0.5 + 0.5 * sin(theta) * cos(phi)

def bias_to_angle(f):
    return 2 * pi * f

# DQM circuit
def simulate_dqm(theta_deg, phi_deg):
    theta = theta_deg * pi / 180
    phi = phi_deg * pi / 180
    angle = bias_to_angle(directional_field(theta, phi))

    qc = QuantumCircuit(1, 1)
    qc.ry(angle, 0)
    qc.measure(0, 0)

    sim = AerSimulator()
    compiled = transpile(qc, sim)
    job = sim.run(compiled, shots=1024)
    result = job.result()
    return result.get_counts()

# Standard circuit
def simulate_standard():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    sim = AerSimulator()
    compiled = transpile(qc, sim)
    job = sim.run(compiled, shots=1024)
    result = job.result()
    return result.get_counts()

# GUI application
class DQMCompareApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DQM vs Standard Quantum Measurement")
        self.geometry("800x550")

        control_frame = ttk.Frame(self)
        control_frame.pack(pady=10)

        ttk.Label(control_frame, text="θ (degrees):").grid(row=0, column=0)
        self.theta_entry = ttk.Entry(control_frame, width=10)
        self.theta_entry.insert(0, "60")
        self.theta_entry.grid(row=0, column=1)

        ttk.Label(control_frame, text="φ (degrees):").grid(row=0, column=2)
        self.phi_entry = ttk.Entry(control_frame, width=10)
        self.phi_entry.insert(0, "45")
        self.phi_entry.grid(row=0, column=3)

        run_button = ttk.Button(control_frame, text="Run Comparison", command=self.update_plot)
        run_button.grid(row=0, column=4, padx=10)

        self.figure = plt.Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack()

        self.update_plot()

    def update_plot(self):
        try:
            theta = float(self.theta_entry.get())
            phi = float(self.phi_entry.get())
        except ValueError:
            self.ax.clear()
            self.ax.text(0.5, 0.5, "Invalid input", horizontalalignment='center', verticalalignment='center')
            self.canvas.draw()
            return

        counts_dqm = simulate_dqm(theta, phi)
        counts_std = simulate_standard()

        self.ax.clear()
        labels = list(set(counts_dqm.keys()).union(set(counts_std.keys())))
        dqm_values = [counts_dqm.get(k, 0) for k in labels]
        std_values = [counts_std.get(k, 0) for k in labels]

        x = range(len(labels))
        self.ax.bar([i - 0.2 for i in x], std_values, width=0.4, label='Standard')
        self.ax.bar([i + 0.2 for i in x], dqm_values, width=0.4, label='DQM')
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(labels)
        self.ax.set_title(f"DQM vs Standard (θ={theta}°, φ={phi}°)")
        self.ax.set_ylabel("Counts")
        self.ax.legend()
        self.canvas.draw()

if __name__ == "__main__":
    app = DQMCompareApp()
    app.mainloop()