import numpy as np
import matplotlib.pyplot as plt

Amplitude = float(input('Enter amplitude: '))
frequency = int(input('Enter frequency: '))
phi_degree = int(input('Enter Signal phase in degree: '))

# Signal period

T = 1/frequency

# Signale Root Mean Square

Amplitude_RMS = Amplitude/np.sqrt(2)

# Initial phase angle in radians

phi_rad = phi_degree/180 * np.pi

t = np.linspace(0, T, num=1000)

signal = Amplitude * np.sin(2*np.pi * frequency * t + phi_rad)


plt.title('Signal')
plt.plot(t, signal, 'b')
plt.xlabel('Time [s]')
plt.ylabel('Voltage [V]')
plt.grid()
plt.show()
