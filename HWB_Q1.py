import numpy as np
import matplotlib.pyplot as plt  

#SINE WAVE
frequencia=17
numero_amostras=1024
valor_pico=1
taxa_amostragem=0.0001
nivel_dc=0

periodo = 1.0 / frequencia
omega = np.pi * 2.0 / periodo
 
tempo = np.arange(start=0, stop=numero_amostras*taxa_amostragem,
step=taxa_amostragem, dtype=np.float)
valor_sinal = valor_pico * np.sin(tempo * omega) + nivel_dc
 
plt.plot(valor_sinal)
plt.show()


##NOISE
  
limitesuperior = 5.0
limiteinferior = -5.0
numeropontos = 450
 
noise= np.random.uniform(low=limiteinferior, high=limitesuperior, size=numeropontos)
 
plt.plot(noise)
plt.show()


##AUTOCORRELATION

AC = np.correlate(valor_sinal, noise, mode="full")
#print AC[AC.size/2:]

plt.plot(AC)
plt.show()