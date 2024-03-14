import matplotlib.pyplot as plt
import numpy as np

R = 1000
C = 100E-9

tau = R*C
fc = 1/(2*np.pi*tau)

print("Frequenza di taglio (cut frequency):", fc, "Hz")

#Faccio una spazzata delle frequenze da una decade sotto fc ad una decade sopra fc (1000 punti)
f = np.linspace(0.1*fc, 10*fc, 100)

#Amplificazione introdotta dal circuito (se minore di uno attenua essendo moltiplicativo)
A = (1/np.sqrt(1+(f*f)/(fc*fc)))

#sfasamento introdotto alle varie freqeunze
sfasamento = -np.arctan(f/fc)

#Stampo cento valori significativi dell'amplificszione
print("\n\nfrequenza", "\t", "amplificazione")
for i in range(0, 100):
    print("{:8}".format(np.round(f[i], 2)), "\t", np.round(A[i], 3))

#Stampo cento valori significativi dello sfasamento
print("frequenza", "\t", "sfasamento")
for i in range(0, 100):
    print("{:8}".format(np.round(f[i], 2)), "\t", np.round((sfasamento[i]/np.pi)*180, 3))

plt.figure(1)
plt.title('Amplificazione del bipolo')
plt.plot(f, A, 'g')
plt.grid(True)
plt.ylabel('Amplificazione')
plt.xlabel('Frequenza [Hz]')

plt.show()

plt.figure(2)
plt.title('Sfasamento del bipolo')
plt.plot(f, (sfasamento /np.pi)*180, 'blue')
plt.grid(True)
plt.ylabel('Sfasamento')
plt.xlabel('Frequenza [Hz]')

plt.show()

plt.figure(3)
plt.title('Amplificazione del bipolo in decibel')
plt.plot(np.log10(f), 20*np.log10(A), 'g')
plt.grid(True)
plt.ylabel('Amplificazione')
plt.xlabel('log(f)')

plt.show()

plt.figure(4)
plt.title('Sfasamento del bipolo')
plt.plot(np.log10(f), (sfasamento /np.pi)*180, 'blue')
plt.grid(True)
plt.ylabel('Sfasamento')
plt.xlabel('log(f)')

plt.show()
