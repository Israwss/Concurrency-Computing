from threading import Thread, Condition
import time
import csv

class Computadora:
    def __init__(self, nombre='', pais_origen='', num_cores=0, ram='', almacenamiento='', teraflops=0.0, sistema_operativo=''):
        self.nombre = nombre
        self.pais_origen = pais_origen
        self.num_cores = num_cores
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.teraflops = teraflops
        self.sistema_operativo = sistema_operativo

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"País de Origen: {self.pais_origen}")
        print(f"Número de Cores: {self.num_cores}")
        print(f"RAM: {self.ram}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"TeraFLOPS: {self.teraflops}")
        print(f"Sistema Operativo: {self.sistema_operativo}")



buffer=[]

# Tamaño del buffer.
MAX_NUM = 4

cabecera = ["Nombre", "País de Origen", "Número de Cores", "RAM", "Almacenamiento", "TeraFLOPS", "Sistema Operativo"]
base=input("Ingresa el nombre del archivo CSV: ")


with open(f"C:/Users/Flash/OneDrive - Facultad de Ingeniería UNAM/Computo Concurrente/Practicas/{base}.csv", mode="w", newline="") as archivo_csv:
    escritor = csv.writer(archivo_csv)
    escritor.writerow(cabecera)


# Objeto condición.
condition = Condition()


##### CLASES PRODUCTOR Y CONSUMIDOR #####

# Clase Productor.

class Productor(Thread):
    def run(self):
        
        # Variables
        computadora = Computadora()
        global buffer
        num = 0
        retardo = 0.5
        
        while num <4:
            
            # Entra al monitor
            condition.acquire()

            # Verifica si el buffer está lleno.
            if len(buffer) == MAX_NUM:
                print("Buffer lleno, Productor esperando")

                retardo = retardo + 1
                # Espera que el comsumidor consuma un dato.
                condition.wait()
                
                print ("Espacio en el buffer, el consumidor notificó al Productor")

            # Agrega un dato al buffer, al final del dato anterior.
            imprimir_en_recuadro("Agregue una computadora al buffer ")

            computadora.nombre = input("Nombre: ")
            computadora.pais_origen = input("País de Origen: ")
            computadora.num_cores = int(input("Número de Cores: "))
            computadora.ram = input("RAM: ")
            computadora.almacenamiento = input("Almacenamiento: ")
            computadora.teraflops = float(input("TeraFLOPS: "))
            computadora.sistema_operativo = input("Sistema Operativo: ")

            buffer.append(computadora)

            imprimir_en_recuadro("Dato producido:")
            computadora.mostrar_info()
            renglon = [computadora.nombre, 
                       computadora.pais_origen, 
                       computadora.num_cores, 
                       computadora.ram, 
                       computadora.almacenamiento, 
                       computadora.teraflops, 
                       computadora.sistema_operativo]

            with open("C:/Users/Flash/OneDrive - Facultad de Ingeniería UNAM/Computo Concurrente/Practicas/computadoras.csv", mode="a", newline="") as archivo_csv:
                escritor = csv.writer(archivo_csv)
                escritor.writerow(renglon)

            num = num + 1
            

            # Notifica que se agregó un dato al buffer.
            condition.notify()

            # Sale del monitor.
            condition.release()

            # Duerme.
            time.sleep(retardo)
            
# Clase Consumidor.

class Consumidor(Thread):
    def run(self):

        # Variables
        global buffer
        retardo = 1
        computadoras_consumidas = 0
        
        while computadoras_consumidas < 4:

            # Entra al monitor.
            condition.acquire()

            # Verifica si el buffer está vacío.
            if not buffer:
                print("Buffer vacío, Consumidor esperando")
                
                 # Espera que el Productor agregue más datos.
                condition.wait()
                
                print("El Productor agregó un dato al buffer y lo notificó al Consumidor")

            # Saca el primer dato y lo borra del buffer.
            computadora = buffer.pop(0)
            
            imprimir_en_recuadro("Dato consumido:")
            computadora.mostrar_info()
            computadoras_consumidas = computadoras_consumidas + 1


            # Notifica que se sacó un dato del buffer.
            condition.notify()

            # Sale del monitor.
            condition.release()

            # Duerme.
            time.sleep(retardo)


def imprimir_en_recuadro(texto):
    longitud = len(texto) + 4
    print("+" + "-" * longitud + "+")
    print("|  " + texto + "  |")
    print("+" + "-" * longitud + "+")



##### INICIO #####
productor = Productor()
consumidor = Consumidor()

productor.start()
consumidor.start()

# Espera a que terminen el productor y consumidor
productor.join()
consumidor.join()

# Imprimir contenido del archivo CSV
imprimir_en_recuadro("Computadoras")
with open("C:/Users/Flash/OneDrive - Facultad de Ingeniería UNAM/Computo Concurrente/Practicas/computadoras.csv", mode="r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    for linea in lector:
        print(linea)
