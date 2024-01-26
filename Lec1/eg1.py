# Importing the 'Qiskit' Module
# Importing the 'Qiskit' Module
from qiskit import *
from qiskit import IBMQ
# paste the api code in 'apostrophes'
#you only need to save the account once, from the next time just load the account.
IBMQ.save_account('8d9fd4cfb1139b39e920a5e17a2d932dcf89a73f3c9441d31cf617139f3cb47ac4eb912c2ada92145a2c9bef7d5c22ca825b5cbe3a6590b599bbce8872f1d216')
IBMQ.load_account()
# Creating a Quantum circuit
circuit = QuantumCircuit(2,2)
# To view the circuit, we use the 'draw()' funcction.
print(circuit)
circuit.draw()
print(circuit.draw())

