import matplotlib.pyplot as plt
import numpy as np

L = 1.0
x = np.linspace(0, L, 200)

def psi(n, x, L):
    return np.sqrt(2/L) * np.sin((n * np.pi * x) / L)

prob_n1 = psi(1, x, L)**2
prob_n2 = psi(2, x, L)**2

plt.figure(figsize=(12,6))
plt.plot(x, prob_n1, label="Ground State (n=1)", color='red')
plt.plot(x, prob_n2, label="Excited State (n=2)", color='blue')

plt.title("Quantum Probability of Finding a Particle")
plt.xlabel("Position (x) inside the box")
plt.ylabel("Probability |ψ(x)|²")
plt.legend()
plt.show()