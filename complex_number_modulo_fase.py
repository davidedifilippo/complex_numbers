mport numpy as np

c1_M = input("Inserire il modulo del numero complesso: ")
c1_phi = input("Inserire la fase del numero complesso in gradi: ")

c1_M = float(c1_M)
c1_phi = float(c1_phi)
c1_phi_rad = (c1_phi/180) * np.pi

# Si ricostruisce il numero in formato cartesiano

c1 = c1_M * (np.cos(c1_phi_rad) + np.sin(c1_phi_rad)*1j)

print("Numero inserito: ", c1)

print("Coordinate cartesiane: ")
print("x=", c1.real)
print("x=", c1.imag)

print("Coordinate polari: ")
print("Modulo=", c1_M)
print("Angolo=", (c1_phi/np.pi) * 180)



