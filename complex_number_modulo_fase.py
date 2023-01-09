import numpy as np
from complex_plane import complex_plane2

c1_M = input("Inserire il modulo del numero complesso: ")
c1_phi = input("Inserire la fase del numero complesso in gradi: ")

c1_M = float(c1_M)
c1_phi = float(c1_phi)
c1_phi_rad = (c1_phi/180.0) * np.pi

# Si ricostruisce il numero in formato cartesiano

c1 = c1_M * (np.cos(c1_phi_rad) + np.sin(c1_phi_rad)*1j)


print("Numero inserito: ", np.round(c1, 2))

print("Coordinate cartesiane: ")
print("x=", np.round(c1.real,2))
print("y=", np.round(c1.imag,2))

print("x=", c1.imag)

print("Coordinate polari: ")
print("Modulo=", c1_M)
print("Angolo=", c1_phi)





