import numpy as np
from complex_plane import complex_plane2

c1 = input("Inserire un numero complesso: ")
c1 = complex(c1)

# Coordinate cartesiane del numero

c1_x = np.real(c1)
c1_y = np.imag(c1)

# Coordinate polari (M, phi)
c1_M = abs(c1)
c1_phi = np.angle(c1)

print("Numero inserito: ", c1)

print("Coordinate cartesiane: ")
print("x=", c1_x)
print("x=", c1_y)

print("Coordinate polari: ")
print("Modulo=", c1_M)

print("Angolo=", (c1_phi/np.pi) * 180)


complex_plane2([c1])
