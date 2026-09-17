import numpy as np
from scipy.constants import G
import matplotlib.pyplot as plt

mass_black_hole = 1.989e30 * 10 #10 solar mass
mass_ship = 5000 

distance = np.linspace(10000e3, 100000e3, 100)

force = G * (mass_black_hole * mass_ship) / (distance**2)

plt.figure(figsize=(7, 4))
plt.plot(distance / 1000, force, color='black', linewidth=2)

plt.title("Black Hole Gravitational Pull")
plt.xlabel("Distance from Black Hole (km) ")
plt.ylabel('Gravitational Force (Newtons) ')
plt.fill_between(distance / 1000, force, color='blue', alpha=0.3)
plt.show()