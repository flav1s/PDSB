import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack, signal

f1 = 50
f2 = 400
f3 = 700
fs = 2000     # taxa de amostragem
Ts = 1.0/fs  # intervalo de amostragem

#-----------------------------------#
#               Sinal               #
#-----------------------------------#

n = np.arange(0,1,Ts) # vetor de tempo
s = np.sin(2 * np.pi * f1 * n) + np.sin(2 * np.pi * f2 * n) + np.sin(2 * np.pi * f3 * n) # sinal

# Funcao no Tempo
plt.subplot(2, 2, 1)
plt.plot(n,s)
plt.grid()
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude');

#-----------------------------------#
#               Filtro              #
#-----------------------------------#
flc = 300.0
fhc = 500.0
fc = fhc - flc # largura da banda de passagem
rc_db = 0.1 # ripple da banda de passagem (dB)
df = 100.0 # largura da banda de transicao
sba_db = 60 # atenuacao da banda de passagem (dB)

# Tipo de janela
rc = 10 ** (rc_db/20) # sigma 1
sba = 10 ** (-sba_db/20) # sigma 2
sigma = min(rc,sba) # sigma minimo = usado para definicao do filtro
print("sigma = " + str(sigma))

# Tamanho da janela
dw = ((2.0 * np.pi) * (df/fs)) # Banda de transicao (angular)
M = ((12.0 * np.pi) / dw) # numero de coeficientes do filtro (Blackman)
print("M = " + str(M))
wn = []
for a in range(int(M)):
    wn.append(0.42 - 0.5 * np.cos((2*a*np.pi)/M) + 0.08 * np.cos((4*a*np.pi)/M))

# Filtro ideal apropriado
whc = fhc * np.pi / (fs / 2)  # high-pass normalize
print("wcu/pi = " + str(whc/np.pi))
wlc = flc * np.pi / (fs / 2)  # low-pass normalize
print("wcl/pi = " + str(wlc/np.pi))
hc = []
for a in range(int(M)):
    hc.append(whc/np.pi * np.sinc((whc*(a-60))/np.pi) - wlc/np.pi * np.sinc((wlc*(a-60))/np.pi)) # Resposta ao impulso do filtro

# Aplicar filtro no tempo
h = []
for a in range(int(M)):
    h.append(wn[a]*hc[a])

# Espectro do filtro
H = fftpack.fft(h)
H_db = 20*np.log10(np.abs(H))
freqs = fftpack.fftfreq(len(H)) * fs # vetor de frequencia scipy

# Plot filtro
plt.subplot(2, 2, 3)
plt.plot(freqs, H_db)
plt.xlabel("Frequencia[Hz]")
plt.ylabel("Magnitude [dB]")
plt.grid()

#-----------------------------------#
#               fft                 #
#-----------------------------------#

S = fftpack.fft(s,int(M)) # fft scipy
freqs = fftpack.fftfreq(len(S)) * fs # vetor de frequencia scipy
# freqs = (fs/len(s)) * range(0, len(s)) # vetor de frequencia manual

# Plot Espectro
plt.subplot(2, 2, 2)
plt.stem(freqs, np.abs(S))
plt.grid()
plt.xlabel('Frequencia[Hz]')
plt.ylabel('Magnitude')

#-----------------------------------#
#          Aplicar filtro           #
#-----------------------------------#
SF = []
for a in range(len(S)):
    SF.append(S[a]*H[a])
plt.subplot(2, 2, 4)
plt.stem(freqs,np.abs(SF))
plt.xlabel("Frequencia[Hz]")
plt.ylabel("Magnitude")
plt.grid()
plt.show()