import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Abrir o sinal
data = []
with open('ECG01_5min@240Hz.dat', 'r') as f:
    d = f.readlines()
    for i in d:
        data.append([float(i)])

data = np.array(data)
fs = data.size / (5.0 * 60.0) # frequencia de amostragem
T = np.divide(range(data.size), fs)

# Plot sinal ruidoso
plt.figure()
plt.plot(T,data)
plt.title("Sinal com ruido")
plt.ylabel("Amplitude")
plt.xlabel("Tempo [s]")
plt.grid()

t = 10 # tempo em segundos
x = np.divide(range(int(t*fs)), fs)
y = data[0:int(t*fs)]

# Plot t segundos de sinal ruidoso
plt.figure()
plt.plot(x, y)
plt.title("Intervalo de " + str(t) + " segundos")
plt.ylabel("Amplitude")
plt.xlabel("Tempo [s]")
plt.grid()

# Filtro Notch
f0 = 60.0  # frequencia a ser removida do sinal
Q = 1.0  # Quality factor
w0 = f0/(fs/2)  # frequencia normalizada

b, a = signal.iirnotch(w0, Q)
y_f = signal.filtfilt(b, a, np.ravel(data))
tf = signal.TransferFunction(b, a)

# Plot sinal ruidoso
plt.figure()
plt.plot(T,y_f)
plt.title("Sinal filtrado")
plt.ylabel("Amplitude")
plt.xlabel("Tempo [s]")
plt.grid()

b, a = signal.iirnotch(w0, Q)
y_t = signal.filtfilt(b, a, np.ravel(y))

# Plot t segundos de sinal filtrado
plt.figure()
plt.plot(x, y_t)
plt.title("Intervalo de " + str(t) + " segundos: Sinal filtrado")
plt.ylabel("Amplitude")
plt.xlabel("Tempo [s]")
plt.grid()

# Resposta da frequencia
w, h = signal.freqz(b, a)
# Gerando eixo da frequencia
freq = w*fs/(2*np.pi)

# Plot filtro
fig, ax = plt.subplots(2, 1, figsize=(8, 6))
ax[0].plot(freq, 20*np.log10(abs(h)), color='blue')
ax[0].set_title("Resposta na Frequencia")
ax[0].set_ylabel("Amplitude (dB)", color='blue')
ax[0].grid()

ax[1].plot(freq, np.unwrap(np.angle(h))*180/np.pi, color='green')
ax[1].set_ylabel("Angulo (graus)", color='green')
ax[1].set_xlabel("Frequencia (Hz)")
ax[1].grid()
plt.show()