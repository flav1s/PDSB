import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
import FIRFilter as ff

f1 = 750
f2 = 2500
f3 = 3250

fs = 6500.0  # taxa de amostragem
Ts = 1.0/fs # intervalo de amostragem
t = np.arange(0,1,Ts) # vetor de tempo
s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t) + np.sin(2 * np.pi * f3 * t) # sinal

# Funcao no Tempo
plt.figure()
plt.title("Sinal")
plt.plot(t,s)
plt.grid()
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

# fft
X = fftpack.fft(s)
freqs = fftpack.fftfreq(len(s)) * fs

# Espectro
plt.figure()
plt.title("Espectro Sinal")
plt.stem(freqs, np.abs(X))
plt.xlabel('Frequencia[Hz]')
plt.ylabel('Magnitude')
plt.grid()

filter = ff.FIRFilter(300.0, 500.0, 0.1, 100.0, 60.0, fs) # low_border, high_border, ripple, transition_band, band_pass_attenuation, fs
filter.fft(len(X))
S = filter.apply_filter_frequency(X)

# ifft
plt.figure()
plt.plot(t, np.abs(np.fft.ifft(S)))
plt.title("Sinal Filtrado")
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

