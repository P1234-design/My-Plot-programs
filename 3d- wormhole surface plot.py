import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

r = np.linspace(0.1, 2, 100)
theta = np.linspace(0, 2 * np.pi, 100)

R, Theta = np.meshgrid(r, theta)

X = R * np.cos(Theta)
Y = R * np.sin(Theta)

Z = -1 / R

surf = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='black')

ax.set_title("Hypothetical WormHole Space time Distortion")
ax.set_zlim(-10, 0)
plt.show()

                