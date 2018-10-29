import numpy as np
import matplotlib.pyplot as plt

T = 1
x = np.exp(-0.5 * np.arange(0, 32*T))
h = [0, 1.5, 0.75, 0.375, 0.1875, 0.09375, 0.046875, 0.0234375]
y = np.convolve(x,h)

plt.subplot(3,1,1)
plt.stem(x)
plt.grid()
plt.subplot(3,1,2)
plt.stem(h)
plt.grid()
plt.subplot(3,1,3)
plt.stem(y)
plt.grid()
plt.show()

