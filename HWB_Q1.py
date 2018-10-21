import numpy as np
import matplotlib.pyplot as plt  

# Sinal
class Signal:
    def __init__(self, frequency, vpp, sample_rate, dc_level):
        self.f = frequency # Frequencia
        self.w = 2.0 * np.pi * frequency # Frequencia Angular
        self.a = vpp / 2.0 # Amplitude
        self.fs = sample_rate # Frequencia de Amostragem
        self.ws = 2.0 * np.pi * sample_rate # Frequencia de Amostragem Normalizada
        self.dc = dc_level
    
    def x(self, start, end):
        return np.arange(start, end, 1/self.ws, np.float) # Eixo X
    
    def y(self, x):
        return self.a * np.sin(x * self.w) + self.dc # Eixo Y
# Ruido
class Noise:
    def __init__(self, vpp, dc_level, size):
        self.low = dc_level - vpp/2 # Valor Minimo
        self.high = dc_level + vpp/2 # Valor Maximo
        self.size = size # Tamanho do Sinal
        self.y = np.random.uniform(self.low, self.high, self.size) # Sinal Ruidoso
        
def autocorrelate(signal):
    # Media
    avg = np.median(signal)
    # avg = float()
    # for x in signal:
    #    avg += x
    # avg = avg/len(signal)
    print ("Avg = " + str(avg))
    # Variancia
    var = np.var(signal)
    # var = float()
    # for x in norm:
    #     var += abs(x)**2
    # var = var/len(signal)
    print ("Var = " + str(var))
    # Normalizacao
    norm = signal
    # norm = signal-avg
    # norm = (signal-avg)/var

    # Autocorelacao
    #result = np.correlate(x, x, mode='full')
    result = np.empty([len(signal)])
    for j in range(len(signal)):
        for n in range(len(signal)):
            if (n+j) < len(signal):
                result[j] += (norm[n]*norm[n+j])
    #result = result/(len(signal)*var)
    return result

# Figure
plt.figure(0)
# Sinal
signal = Signal(17, 1, 170,0)
x = signal.x(-np.pi, np.pi)
y = signal.y(x)
plt.subplot(311)
plt.plot(x, y)
plt.ylabel("Sinal")
plt.title("Adicao de ruido")
# Ruido
noise = Noise(5, 0, len(x))
plt.subplot(312)
plt.plot(x, noise.y)
plt.ylabel("Ruido")
# Sinal ruidoso
signal_1 = np.sum([y,noise.y], axis=0)
plt.subplot(313)
plt.plot(x, signal_1)
plt.ylabel("Sinal+Ruido")
#
plt.show(False)

# Figure
plt.figure(1)
# Autocorrelacao: Sinal
ac_s_1 = np.correlate(y, y, mode='full') # Autocorrelacao - Numpy
ac_s_2 = autocorrelate(y) # Autocorrelacao - Manual
ac_s_3 = ac_s_2/ac_s_2[0] # Normalizacao
plt.subplot(321)
plt.plot(ac_s_1)
plt.title("Autocorrelacao: Sinal")
plt.ylabel("Numpy")
plt.subplot(323)
plt.plot(ac_s_2)
plt.ylabel("Manual")
plt.subplot(325)
plt.plot(ac_s_3)
plt.ylabel("Normalizado")
# Autocorrelacao: Sinal + Ruido
ac_sn_1 = np.correlate(signal_1, signal_1, mode='full') # Autocorrelacao - Numpy
ac_sn_2 = autocorrelate(signal_1) # Autocorrelacao - Manual
ac_sn_3 = ac_sn_2/ac_sn_2[0] # Normalizacao
plt.subplot(322)
plt.plot(ac_sn_1)
plt.title("Autocorrelacao: Sinal+Ruido")
plt.subplot(324)
plt.plot(ac_sn_2)
plt.subplot(326)
plt.plot(ac_sn_3)

plt.show()
