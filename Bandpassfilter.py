import numpy as np
import matplotlib.pyplot as plt

R = 1000
C = 159.2e-12
f = np.logspace(0, 7, 1000) # 0 to 10 MHz
w = 2 * np.pi * f

gL_db = 20 * np.log10(1 / np.sqrt(1 + (w*R*C)**2))

plt.semilogx(f, gL_db)
plt.axvline(1e6, color='r', linestyle='--', label='1 MHz Corner') 
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.title('Low-Pass Filter Gain')
plt.legend()
plt.show()

R = 10000  
C = 15.92e-9
f = np.logspace(0, 7, 1000)
w = 2 * np.pi * f

gH_db = 20 * np.log10(w*R*C / np.sqrt(1 + (w*R*C)**2))

plt.semilogx(f, gH_db)
plt.axvline(10000, color='r', linestyle='--', label='10 kHz Corner')
plt.xlabel('Frequency (Hz)') 
plt.ylabel('Gain (dB)')
plt.title('High-Pass Filter Gain')
plt.legend()
plt.show()

g_db = gL_db + gH_db

plt.semilogx(f, g_db)
plt.axvline(10000, color='g', linestyle='--', label='10 kHz Lower Corner')
plt.axvline(1e6, color='r', linestyle='--', label='1 MHz Upper Corner')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)') 
plt.title('Band-Pass Filter Gain')
plt.legend()
plt.show()
