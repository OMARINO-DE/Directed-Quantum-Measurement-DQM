#!/bin/bash

echo "🌐 Creating Python virtual environment: dqm-env"
python3 -m venv dqm-env

echo "✅ Activating environment..."
source dqm-env/bin/activate

echo "📦 Installing compatible Qiskit and IBM provider versions..."
pip install --upgrade pip
pip install "qiskit==1.0.2" "qiskit-ibm-provider==0.10.0" matplotlib numpy

echo "✅ DQM environment is ready to use!"