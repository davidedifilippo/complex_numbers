Importiamo la libreria numpy:     
     
     import numpy as np

Diamo la possibilità di inserire la frequenza di lavoro, la resistenza e la capacità del condensatore:

    frequenza = input("Inserire la frequenza di lavoro:")
    frequenza = float(frequenza)
    
    tensione = input("Inserire la tensione di alimentazione:")
    tensione = float(tensione)
    
    tensione = input("Inserire la fase del generatore:")
    tensione = float(tensione)
    
    frequenza = input("Inserire la resistenza:")
    resistenza = float(resistenza)
    
    capacità = input("Inserire la capacità in microfarad:")
    capacità = float(capacità) * pow(10,-6)
    
  
Bisogna determinare l'impedenza resistiva e l'impedenza capacitiva:
 
      ZR = R
      
      ZC = -1j*C
 
Poi calcoliamo l'impedenza serie vista dal generatore:

      Zserie = ZR + ZC 
      
Si calcola la corrente utilizzando al egge di Ohm generalizzata:

      I= tensione / Zserie
      
 Passiamo ora a disegnare nel tempo la tensione e la corrente:
 
 
