### Cacolo della tensione di uscita a tre frequenze significative

      import matplotlib.pyplot as plt
      import numpy as np

#Parametri del filtro

R = 1000
C = 100E-9

tau = R*C
fc = 1/(2*np.pi*tau)

#Segnale di ingresso

V_max = 10
f_in = 159.1 #frequenza di taglio
T_in = 1/f_in #periodo

t = np.linspace(0, 2*T_in, 1000)

v_in = V_max * np.sin(2*np.pi*f_in*t)

#Uscita del filtro
v_out = V_max *((1/np.sqrt(1+(f_in*f_in)/(fc*fc))))*np.sin(2*np.pi*f_in*t-np.arctan(f_in/fc))


plt.figure(1)
plt.title('Tensione di ingresso e tensione di uscita')
plt.plot(t, v_in, 'g')
plt.plot(t, v_out, 'b')
plt.grid(True)
plt.ylabel('volt')
plt.xlabel('tempo')

plt.show()


f_in = 1591 #frequenza di taglio
T_in = 1/f_in #periodo

t = np.linspace(0, 2*T_in, 1000)
v_in = V_max * np.sin(2*np.pi*f_in*t)

v_out = V_max *((1/np.sqrt(1+(f_in*f_in)/(fc*fc))))*np.sin(2*np.pi*f_in*t-np.arctan(f_in/fc))

plt.figure(2)
plt.title('Tensione di ingresso e tensione di uscita')
plt.plot(t, v_in, 'g')
plt.plot(t, v_out, 'b')
plt.grid(True)
plt.ylabel('volt')
plt.xlabel('tempo')

plt.show()


f_in = 15915 #frequenza di taglio
T_in = 1/f_in #periodo

t = np.linspace(0, 2*T_in, 1000)
v_in = V_max * np.sin(2*np.pi*f_in*t)

v_out = V_max *((1/np.sqrt(1+(f_in*f_in)/(fc*fc))))*np.sin(2*np.pi*f_in*t-np.arctan(f_in/fc))

plt.figure(3)
plt.title('Tensione di ingresso e tensione di uscita')
plt.plot(t, v_in, 'g')
plt.plot(t, v_out, 'b')
plt.grid(True)
plt.ylabel('volt')
plt.xlabel('tempo')

plt.show()


