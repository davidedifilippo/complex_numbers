import math
import numpy as np
import matplotlib.pyplot as plt

f = 10000 # frequency - Hertz 
C= 10*pow(10, -6) # Capacity microFarad

Z_C = (1/(1j*2*math.pi*f*C)
Vout = 10
Ic = Vout/Z_C

print('Capacitor Impedance = {:.2f} Ω'.format(Z_C))
print('Current = {:.2f} Ω'.format(Ic))

# Plotting Phasor Diagram

figure = plt.subplots(figsize=(11, 6))
axe = plt.subplot(121)

plt.title('V Phasor Diagram')
axe.quiver(0, 0, np.array((np.real(Vout))), np.array((np.imag(Vout))), units='xy', scale=1, color='blue')


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


axe = plt.subplot(122)

plt.title('I Phasor Diagram ')
axe.quiver(0, 0, np.array((np.real(Ic))), np.array((np.imag(Ic))), units='xy', scale=1, color='orange')


plt.grid()
axe.set_aspect('equal')
axe.spines['left'].set_position('zero')
axe.spines['right'].set_color('none')
axe.spines['bottom'].set_position('zero')
axe.spines['top'].set_color('none')

limit = abs(Ic)
plt.xlim(-limit,limit)
plt.ylim(-limit,limit)
plt.legend("I")


plt.tight_layout()

plt.tight_layout()
plt.show()
