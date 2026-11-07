from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1. Inicialização: Qubits em superposição uniforme
qc = QuantumCircuit(2, 2)
qc.h([0,1])

# 2. Oráculo: Marca o estado alvo |11> (inversão de fase)
qc.cz(0,1)

# 3. Operador de Difusão: Inversão sobre a média
qc.h([0,1])
qc.z([0,1])
qc.cz(0,1)
qc.h([0,1])

# 4. Medição
qc.measure([0,1], [0,1])

# Desenha e salva o circuito
fig_circuito = qc.draw(output='mpl')
fig_circuito.savefig("circuito_grover.png")

# 5. Execução no simulador ideal com semente fixa
sim = AerSimulator()
result = sim.run(qc, shots=1000, seed_simulator=42).result()
counts = result.get_counts()

print("Resultados da medição (1000 shots):", counts)

# Gera e salva o histograma
fig_hist = plot_histogram(counts)
fig_hist.savefig("histograma_grover.png")

# EXIBE as imagens na tela (janelas pop-up)
plt.show()
