# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:49:34 2018

@author: matheus
"""

import numpy as np
import matplotlib.pyplot as plt  

class Signal:
    def __init__(self, frequency, amplitude, sample_rate, dc_level):
        self.f = frequency
        self.w = 2.0 * np.pi * frequency
        self.a = amplitude
        self.fs = sample_rate
        self.ws = 2.0 * np.pi * sample_rate
        self.dc = dc_level
    
    def x(self, start, end):
        return np.arange(start, end, 1/self.ws, np.float)
    
    def y(self, x):
        return self.a * np.sin(x * self.w) + self.dc
    
class Noise:
    def __init__(self, vpp, dc_level, size):
        self.low = dc_level - vpp
        self.high = dc_level + vpp
        self.size = size
        self.y = np.random.uniform(self.low, self.high, self.size)
        
def autocorrelate(x):
    result = np.correlate(x, x, mode='full')
    return result[result.size/2:]
        
## Sinal
signal = Signal(17, 1, 170,0)
x = signal.x(-np.pi, np.pi)
y = signal.y(x)
plt.plot(x, y)
plt.show()

# Ruído
noise = Noise(1, 0, len(x))
plt.plot(x, noise.y)
plt.show()

# Sinal ruidoso
signal_1 = np.sum([y,noise.y], axis=0)
plt.plot(x, signal_1)
plt.show()

# Autocorrelação
ac = autocorrelate(y)
plt.plot(ac)
plt.show()