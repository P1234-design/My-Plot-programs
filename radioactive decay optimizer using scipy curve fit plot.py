import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def decay_model(t, N0, decay_constant):
    return N0*np.exp(-decay_constant*t)

time_data = np.array([0, 1, 2, 3, 4, 5])
quantity_data = np.array([100, 62, 38, 25, 14, 9])

best_values, _ = curve_fit(decay_model, time_data, quantity_data)
N0_fit, lambda_fit = best_values

print(f'Calculated Initial Quantity: {round(N0_fit, 2)}')
print(f'calulated Decay Constant (λ): {round(lambda_fit,4)}')


time_smooth = np.linspace(0, 5, 50)
quantity_smooth = decay_model(time_smooth, N0_fit, lambda_fit)

plt.scatter(time_data, quantity_data, color='red', label='Real Lab Data (Dots)')
plt.plot(time_smooth, quantity_smooth, color='blue', label='AI Best fit LIne')
plt.title("Radioactive Decay Curve Fitting")
plt.legend()
plt.show()