import numpy as np
import matplotlib.pyplot as plt

def plot_projectile(u, theta_degrees):
    g = 9.8 

    theta = np.radians(theta_degrees)

    t_flight = (2 * u * np.sin(theta)) / g

    t = np.linspace(0, t_flight, 100)

    x = u * np.cos(theta) * t
    y = (u * np.sin(theta) * t) - (0.5 * g * t**2)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, color='red', label=f'Angle: {theta_degrees}°')

    plt.title("Physics: Projectile Trajectory")
    plt.xlabel("Distance (X-axis)")
    plt.ylabel("Height (Y-axis)")
    plt.axhline(0, color='black', linewidth=1) 
    plt.legend()
    plt.grid(True) 
    plt.show()

plot_projectile(456, 30)