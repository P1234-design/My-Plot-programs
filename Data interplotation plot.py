import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x_hours = np.array([0, 2, 4, 6, 8])
y_temp = np.array([20, 25, 22, 30, 28])

f_cubic = interp1d(x_hours, y_temp, kind='cubic')

x_smooth_hours = np.linspace(0, 8, 30)
y_smooth_temp = f_cubic(x_smooth_hours)

plt.plot(x_hours, y_temp, 'o', color='red', label='Known Data(Recording)')
plt.plot(x_smooth_hours, y_smooth_temp, '-', color='green', label='Cubic Interpolated(Gussed) Path')
plt.title('Missing Temperature Data Recovery')
plt.legend()
plt.show()

# Remark: If any experiment records are not found, then guess(inerpoate) by scipy