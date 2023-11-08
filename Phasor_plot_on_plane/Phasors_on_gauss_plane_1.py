
import math
import numpy as np
import matplotlib.pyplot as plt

c1 = input("Inserire i dati del fasore: ")
c1 = complex(c1)

#ad esempio c1 = 10j


# Plotting Phasor Diagram

figure = plt.subplots(figsize=(11, 6))
axe = plt.subplot(121)

plt.title('Phasor Diagram')
axe.quiver(0, 0, np.array((np.real(c1))), np.array((np.imag(c1))), units='xy', scale=1, color='red')


plt.grid()
axe.set_aspect('equal')
axe.spines['left'].set_position('zero')
axe.spines['right'].set_color('none')
axe.spines['bottom'].set_position('zero')
axe.spines['top'].set_color('none')

limit = abs(c1)
plt.xlim(-limit,limit)
plt.ylim(-limit,limit)
plt.legend("V")


plt.tight_layout()
plt.show()
