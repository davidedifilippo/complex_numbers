import numpy as np
import matplotlib.pyplot as plt

# set inductance value
C = 10 * pow(10, -6)

frequency = np.linspace(0, 1000000, num=1000)

# Inductive Reactance values

XC = 1/(2 * np.pi * frequency * C)

plt.title('XC Capacitive Reactance')
plt.plot(frequency, XC, 'orange')
plt.xlabel('Frequency')
plt.ylabel('Ohm')
plt.grid()
plt.show()
