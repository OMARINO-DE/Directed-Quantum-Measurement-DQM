@echo off
echo Creating virtual environment: dqm-env
python -m venv dqm-env

echo Activating environment...
call dqm-env\Scripts\activate

echo Installing compatible Qiskit and IBM provider versions...
pip install --upgrade pip
pip install "qiskit==1.0.2" "qiskit-ibm-provider==0.10.0" matplotlib numpy

echo ✅ DQM environment is ready!
pause