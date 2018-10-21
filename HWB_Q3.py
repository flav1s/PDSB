import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

f1 = 750
f2 = 2500
f3 = 3250

fs = 150.0;  # taxa de amostragem
Ts = 1.0/fs; # intervalo de amostragem
t = np.arange(0,1,Ts) # vetor de tempo
s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t) + np.sin(2 * np.pi * f3 * t)

# Funcao no Tempo
plt.subplot(2, 1, 1)
plt.plot(t,s)
plt.grid()
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude');

# FFT
X = fftpack.fft(s)
freqs = fftpack.fftfreq(len(s)) * fs

# Espectro
plt.subplot(2, 1, 2)
plt.stem(freqs, np.abs(X))
plt.grid()
plt.xlabel('Frequencia[Hz]')
plt.ylabel('Magnitude')
plt.show()