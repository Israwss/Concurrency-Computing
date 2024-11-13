from mpi4py import MPI
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
        print(f"Pais de Origen: {self.pais_origen}")
        print(f"Numero de Cores: {self.num_cores}")
        print(f"RAM: {self.ram}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"TeraFLOPS: {self.teraflops}")
        print(f"Sistema Operativo: {self.sistema_operativo}")

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    base = input("Ingresa el nombre del archivo CSV (sin la extensión): ")

    cabecera = ["Nombre", "País de Origen", "Número de Cores", "RAM", "Almacenamiento", "TeraFLOPS", "Sistema Operativo"]
    with open(f"{base}.csv", mode="w", newline="") as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(cabecera)
else:
    base = None

base = comm.bcast(base, root=0)

if rank == 0:
    while True:
        print("\nProceso 0: comenzando a recopilar datos...")
        computadora = Computadora(
            nombre=input("\nNombre: "),
            pais_origen=input("Pais de Origen: "),
            num_cores=int(input("Numero de Cores: ")),
            ram=input("RAM: "),
            almacenamiento=input("Almacenamiento: "),
            teraflops=float(input("TeraFLOPS: ")),
            sistema_operativo=input("Sistema Operativo: ")
        )

        print("Proceso 0: enviando datos al proceso 1...")
        comm.send(computadora, dest=1)

        continuar = input("¿Desea ingresar otra computadora? (si/no): ").strip().lower()
        if continuar != 'si':
            comm.send(None, dest=1)
            break

elif rank == 1:
    while True:
        computadora = comm.recv(source=0)
        if computadora is None:
            break

        print("Proceso 1: datos recibidos del proceso 0.\n")
        computadora.mostrar_info()

        print("Proceso 1: escribiendo datos en el archivo CSV...")
        with open(f"{base}.csv", mode="a", newline="") as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerow([
                computadora.nombre,
                computadora.pais_origen,
                computadora.num_cores,
                computadora.ram,
                computadora.almacenamiento,
                computadora.teraflops,
                computadora.sistema_operativo
            ])
        print("Proceso 1: datos escritos en el archivo CSV.")


