# Setup Guide for Directed Quantum Measurement (DQM)

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [IBM Quantum Account Setup](#ibm-quantum-account-setup)
4. [Running Experiments](#running-experiments)
5. [Troubleshooting](#troubleshooting)

---

## Prerequisites

- **Python 3.8 or higher**
- **pip** package manager
- **Git** (for cloning the repository)
- **IBM Quantum Account** (free - for cloud experiments)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/OMARINO-DE/Directed-Quantum-Measurement-DQM.git
cd Directed-Quantum-Measurement-DQM
```

### 2. Create Virtual Environment

#### Windows (PowerShell)
```powershell
python -m venv dqm-env
.\dqm-env\Scripts\Activate.ps1
```

Or use the provided script:
```powershell
.\setup_dqm_env.bat
```

#### Linux/macOS
```bash
python3 -m venv dqm-env
source dqm-env/bin/activate
```

Or use the provided script:
```bash
chmod +x setup_dqm_env.sh
./setup_dqm_env.sh
```

### 3. Install Dependencies

```bash
pip install -r requirements_dqm.txt
```

---

## IBM Quantum Account Setup

### Step 1: Create IBM Quantum Account

1. Go to [IBM Quantum](https://quantum.ibm.com/)
2. Click **"Sign up"** (or log in if you already have an account)
3. Complete the registration process (it's free!)

### Step 2: Get Your API Token

1. Log in to [IBM Quantum](https://quantum.ibm.com/)
2. Click on your profile icon (top right)
3. Go to **"Account settings"**
4. Copy your **API token**

### Step 3: Save Your Token

You have two options:

#### Option A: Save Token in Python (Recommended)

Run Python and execute:

```python
from qiskit_ibm_provider import IBMProvider

# Replace 'YOUR_IBM_QUANTUM_TOKEN' with your actual token
IBMProvider.save_account('YOUR_IBM_QUANTUM_TOKEN', overwrite=True)
```

This saves your credentials locally and you won't need to enter them again.

#### Option B: Edit Files Directly

In files like `dqm_ibm_backend.py` and `dqm_ibm_entangled_qiskit2.py`, find this line:

```python
# IBMProvider.save_account('YOUR_IBM_QUANTUM_TOKEN', overwrite=True)
```

Uncomment it and replace `YOUR_IBM_QUANTUM_TOKEN` with your actual token:

```python
IBMProvider.save_account('your_actual_token_here', overwrite=True)
```

**⚠️ IMPORTANT:** Never commit your token to Git! It's already in `.gitignore` but be careful.

### Step 4: Verify Connection

Run a simple test:

```python
from qiskit_ibm_provider import IBMProvider

provider = IBMProvider()
print("Available backends:", provider.backends())
```

If you see a list of quantum backends, you're ready to go!

---

## Running Experiments

### 1. Basic DQM Simulation (No IBM Account Needed)

These experiments run locally on your computer:

```bash
# Pure Python simulation
python DQM.py

# Basic Qiskit simulation
python qm-DQM.py

# Comparison experiment
python dqm_vs_standard_comparison.py

# Entangled pair experiment
python dqm_entangled_pair.py

# Interactive GUI
python dqm_gui_simulator.py
```

### 2. IBM Quantum Cloud Experiments (Requires IBM Account)

These experiments connect to IBM's quantum computers:

```bash
# IBM backend simulation
python dqm_ibm_backend.py

# Entangled pair on IBM
python dqm_ibm_entangled_qiskit2.py

# IBM Kyiv experiments (requires access)
python dqm_ibm_kyiv_runtime.py
python dqm_ibm_kyiv_standard_no_dqm.py
```

**Note:** Some real quantum hardware backends may require additional access permissions.

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'qiskit'`

**Solution:** Make sure your virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements_dqm.txt
```

### Issue: `IBMAccountError: No IBM Quantum credentials found`

**Solution:** You need to save your IBM Quantum token first. See [IBM Quantum Account Setup](#ibm-quantum-account-setup).

### Issue: `Backend 'ibm_kyiv' not found`

**Solution:** Some backends require special access or may be offline. Try using `ibmq_qasm_simulator` instead:

```python
backend = provider.get_backend('ibmq_qasm_simulator')
```

### Issue: Virtual environment activation fails on Windows

**Solution:** You may need to allow script execution:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: Plots don't show up

**Solution:** Make sure matplotlib is configured correctly. You may need to add:
```python
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg'
```

---

## Environment Variables (Optional)

For advanced users, you can set up environment variables:

### Windows
```powershell
$env:QISKIT_IBM_TOKEN="your_token_here"
```

### Linux/macOS
```bash
export QISKIT_IBM_TOKEN="your_token_here"
```

Then modify your scripts to use:
```python
import os
token = os.getenv('QISKIT_IBM_TOKEN')
IBMProvider.save_account(token, overwrite=True)
```

---

## Next Steps

1. Start with the basic simulations to understand DQM
2. Explore the interactive GUI simulator
3. Run experiments on IBM's quantum simulators
4. Try real quantum hardware (when available)
5. Modify parameters and explore the theory
6. Read the [README.md](README.md) for theoretical background

---

## Support

For issues, questions, or contributions:
- Open an issue on [GitHub](https://github.com/OMARINO-DE/Directed-Quantum-Measurement-DQM/issues)
- Contact: Omar Zaror - OMARINO Quantum Research Initiative

---

**Happy Quantum Experimenting! 🚀**
