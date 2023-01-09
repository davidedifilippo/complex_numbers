import numpy as np
import matplotlib.pyplot as plt

# set inductance value
L = 10 * pow(10, -3)

frequency = np.linspace(0, 1000000, num=1000)

# Inductive Reactance values

XL = 2 * np.pi * frequency * L

plt.title('XL Inductive Reactance')
plt.plot(frequency, XL, 'orange')
plt.xlabel('Frequency')
plt.ylabel('Ohm')
plt.grid()
plt.show()
