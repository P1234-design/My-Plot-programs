import numpy as np
import matplotlib.pyplot as plt
from math import pi,sqrt 
def estimate_pi(n_points):
    x = np.random.rand(n_points)
    y = np.random.rand(n_points)
    
    distance = np.sqrt(x**2 + y**2)
    inside_circle = distance <= 1
    
    pi_estimate = 4 * np.sum(inside_circle / n_points)
    return x, y, inside_circle, pi_estimate

N = 1000
x, y, inside,pi_val = estimate_pi(N)

print(f"Estimated Pi: {pi_val}")

plt.figure(figsize=(6,6))
plt.scatter(x[inside], y[inside], color='blue', s=1, label='Inside')
plt.scatter(x[~inside], y[~inside], color='red', s=1, label='Outside')
plt.title(f"Monte Carlo Pi Estimation (N={N})\nResult: {pi_val}")
plt.legend()
plt.show()
                             
                             