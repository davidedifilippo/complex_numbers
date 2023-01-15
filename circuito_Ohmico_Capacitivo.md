Importiamo la libreria numpy:     
     
     import numpy as np
     from complex_plane import complex_plane2
 

Diamo la possibilità di inserire la frequenza di lavoro, la resistenza e la capacità del condensatore:

    frequenza = input("Inserire la frequenza di lavoro:")
    frequenza = float(frequenza)
    
    VG_MAX = input("Inserire la tensione di alimentazione:")
    VG_MAX = float(tensione)
    
    VG_ph = input("Inserire la fase del generatore:")
    VG_ph = float(tensione)
    
    VG = VG_MAX * ((np.cos(VG_ph)+ (np.cos(VG_ph)*1j)
    
    resistenza = input("Inserire la resistenza:")
    resistenza = float(resistenza)
    
    capacità = input("Inserire la capacità in microfarad:")
    capacità = float(capacità) * pow(10,-6)
    
  
Bisogna determinare l'impedenza resistiva e l'impedenza capacitiva:
 
      ZR = R
      
      XC = 1/(2*np.pi*frequenza*C)
      
      ZC = -1j*XC
 
Poi calcoliamo l'impedenza serie vista dal generatore:

      Zserie = ZR + ZC 
      
Si calcola la corrente utilizzando al egge di Ohm generalizzata:

      I= VG / Zserie
      
 Calcoliamo la tensione sul condensatore e sulla resistenza:
 
      VC = ZC*I
      VR = R*I
      
   Disegnamo i fasori sul piano complesso:
 
      complex_plane2([VG, VR, VC, IC])
 

 

