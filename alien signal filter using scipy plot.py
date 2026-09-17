import numpy as np
from scipy.signal import medfilt
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
true_signal = np.sin(x)

noise = np.random.normal(0, 0.5, 100)
noisy_signal = true_signal + noise

clean_signal = medfilt(noisy_signal, kernel_size=11)

plt.figure(figsize=(10, 5))
plt.plot(x, noisy_signal, label="Noisy signal (Space interference)", color='red')
plt.plot(x, clean_signal, label="Filtered Signal (Decoded)", color='green', linewidth=2)

plt.title("Alien Transmission Decoding")
plt.legend()
plt.show()
                         