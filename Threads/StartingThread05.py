##### SUMA DE NÚMEROS DE UNA LISTA USANDO 2 HILOS CON UNA VARIABLE COMPARTIDA #####
##### DECREMENTA 'n' DE 1 EN 1 HASTA 0. SE USA EL MÓDULO THREADING            #####

##### MÓDULOS #####

import time
import threading  


###### Variable global compartida #####

SumaTotal = 0


##### MÉTODOS #####

# Calcula la suma de la primera mitad de números de la lista con 'th1'.

def for1(num,bloqueo):
    n = len(num) * 30
    print("Números calculados por hilo th1:        {:,}".format(len(num)))
    global SumaTotal
    SumaParcial = 0
    print(" Calcula la suma de la primera mitad de números de la lista con 'th1'.")
    
    for i in num: 
        SumaParcial = SumaParcial + i
        
    print(" La suma parcial del hilo 'th1' es:        {:.8e}".format(SumaParcial))

     
    # Cualquier otra operación que dure gran cantidad de tiempo
    while n>0:
        n -= 1
    
    
    # Sección critica

    bloqueo.acquire()
    SumaTotal = SumaTotal + SumaParcial
    bloqueo.release()
    
# Calcula la suma de la segunda mitad de números de la lista con 'th1'.

def for2(num,bloqueo):
    n = len(num) * 30
    print("Números calculados por hilo th2:        {:,}".format(len(num)))
    global SumaTotal
    SumaParcial = 0
    print(" Calcula la suma de la segunda mitad de números de la lista con 'th2'.")
    
    for i in num:  
        SumaParcial = SumaParcial + i

    print(" La suma parcial del hilo 'th2' es:        {:.8e}".format(SumaParcial))

    
    # Cualquier otra operación que dure gran cantidad de tiempo
    while n>0:
        n -= 1
            

   
    # Manda llamar al bloqueo
    bloqueo.acquire()

    # Sección critica
    SumaTotal = SumaTotal + SumaParcial

    # Libera al bloqueo
    bloqueo.release()
    
##### INICIO #####

# Tiempo de inicio
T1 = time.time()

# Crea el objeto bloqueo
bloqueo = threading.Lock()
    
# Lista de números
# La lista va de 0 - 19999999
numeros = list(range(20000000))

# mitad = 10,000,000
mitad = int(len(numeros)/2)

# total = 20,000,000
total = int(len(numeros))


# Creación de los objetos tipo Thread 'th1' y 'th2'.

# La porcion del arreglo de numeros va de 0 - 9,999,999 (en total son 10 millones) 
th1 = threading.Thread(target=for1, args=(numeros[0:mitad],bloqueo))

# La porcion del arreglo de numeros va de 10,000,000 - 19,999,999 (en total son 10 millones) 
th2 = threading.Thread(target=for2, args=(numeros[mitad:total],bloqueo))


# Activación de los hilos 'th1' y 'th2'.

t_activ1 = time.time() # Tiempo de inicio de activación de los hilos.
th1.start()  
th2.start()
t_activ2 = time.time() # Tiempo final de activación de los hilos.

print(f" Tiempo de activación:                        {t_activ2 - t_activ1}")

# El hilo principal espera a que terminen los 2 hilos.

t_esp1 = time.time() # Tiempo de inicio de espera de los hilos.
th1.join()  
th2.join()
t_esp2 = time.time() # Tiempo final de espera de los hilos
print(f" Tiempo de espera de los hilos                {t_esp2 - t_esp1}")

# tiempo final del programa
T2 = time.time()
print(" Nuevamente en el hilo principal")
print(" La summa total es:                            {:.8e}".format(SumaTotal))
print(f" Tiempo total:                                {T2 - T1}")  

