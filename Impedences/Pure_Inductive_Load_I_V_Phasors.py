import math
import numpy as np
import matplotlib.pyplot as plt

f = 10000 # frequency - Hertz 
L= 10*pow(10, -3) # Inductance in milliHenry

Z_L = 1j*2*math.pi*f*L

VL = input("Inserire la tensione complessa: ")
VL = complex(VL)

IL = VL/Z_L

print('Capacitor Impedance = {:.2f} Ω'.format(Z_L))
print('Current = {:.2f} Ω'.format(IL))

# Plotting Phasor Diagram

figure = plt.subplots(figsize=(11, 6))
axe = plt.subplot(121)

plt.title('V Phasor Diagram')
axe.quiver(0, 0, np.array((np.real(VL))), np.array((np.imag(VL))), units='xy', scale=1, color='blue')


plt.grid()
axe.set_aspect('equal')
axe.spines['left'].set_position('zero')
axe.spines['right'].set_color('none')
axe.spines['bottom'].set_position('zero')
axe.spines['top'].set_color('none')

limit = abs(VL)
plt.xlim(-limit,limit)
plt.ylim(-limit,limit)
plt.legend("VL")


axe = plt.subplot(122)

plt.title('I Phasor Diagram ')
axe.quiver(0, 0, np.array((np.real(IL))), np.array((np.imag(IL))), units='xy', scale=1, color='orange')


plt.grid()
axe.set_aspect('equal')
axe.spines['left'].set_position('zero')
axe.spines['right'].set_color('none')
axe.spines['bottom'].set_position('zero')
axe.spines['top'].set_color('none')

limit = abs(IL)
plt.xlim(-limit,limit)
plt.ylim(-limit,limit)
plt.legend("IL")


plt.tight_layout()

plt.tight_layout()
plt.show()
