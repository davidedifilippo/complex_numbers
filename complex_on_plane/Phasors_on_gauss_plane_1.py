# Phasor circuit analysis - pure Capacitive component

import math
import numpy as np
import matplotlib.pyplot as plt

f = 10000

Z_C = (1/(1j* 2*math.pi*f*pow(10, -6)))
Vout = 10j
IC = Vout/Z_C

print('Capacitor Impedance = {:.2f} Ω'.format(Z_C))

# Plotting Phasor Diagram

figure = plt.subplots(figsize=(11, 6))
axe = plt.subplot(121)

plt.title('Phasor Diagram for Voltages')
axe.quiver(0, 0, np.array((np.real(Vout))), np.array((np.imag(Vout))), units='xy', scale=1, color='red')


plt.grid()
axe.set_aspect('equal')
axe.spines['left'].set_position('zero')
axe.spines['right'].set_color('none')
axe.spines['bottom'].set_position('zero')
axe.spines['top'].set_color('none')

limit = abs(Vout)
plt.xlim(-limit,limit)
plt.ylim(-limit,limit)
plt.legend("V")


plt.tight_layout()
plt.show()
