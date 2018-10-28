import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
import FIRFilter as ff

f1 = 75
f2 = 25
f3 = 32

fs = 200.0;  # taxa de amostragem
Ts = 1.0/fs; # intervalo de amostragem
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

filter = ff.FIRFilter(20.0, 35.0, 0.1, 10.0, 20.0, fs) # low_border, high_border, ripple, transition_band, band_pass_attenuation, fs
filter.fft(len(X))
S = filter.apply_filter_frequency(X)

print (len(t))
print (len(np.abs(S)))

# ifft
plt.figure()
plt.plot(t, np.abs(np.fft.ifft(S)))
plt.title("Sinal Filtrado")
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

