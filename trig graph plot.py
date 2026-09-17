import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

plt.figure(figsize=(8, 4))
plt.plot(x,y1,label="Sin Wave",color='blue',linestyle='-')
plt.plot(x,y2,label="Cos Wave",color='red',linestyle='--')
plt.plot(x,y3,label="Tan wave",color='yellow',linestyle='-.')

plt.title("Sin,Cosine and Tanngent")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.grid()

plt.show()