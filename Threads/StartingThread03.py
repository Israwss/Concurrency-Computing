##### CALCULA EL CUADRADO Y EL CUBO DE UNA LISTA USANDO EL HILO PRINCIPAL #####


##### MÓDULOS ##### 

import time


##### Funciones #####

# Calcula el cuadrado de los elementos de un arreglo.
def cal_sqre(num):
    print(" Calcula el cuadrado de los elementos de un arreglo")  
    for n in num:   
        time.sleep(0.3) # Cada iteración espera 0.3 s.  
        print(f" El cuadrado de {n} :  {n * n}")  

# Calcula el cubo de los elementos de una arreglo.
def cal_cube(num):  
    print(" Calcula el cubo de los elementos de un arreglo")  
    for n in num:   
        time.sleep(0.3) # Cada iteración espera 0.3 s.  
        print(f" El cubo de {n} :  {n * n * n}")  


##### Inicio #####

arr = [4, 5, 6, 7, 2]
  
t1 = time.time() # Obtiene el tiempo inicial del programa  
cal_sqre(arr)
cal_cube(arr)
  
print(" Tiempo total del programa :", time.time() - t1)

