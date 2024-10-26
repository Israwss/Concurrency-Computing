##### IMPRIME EL NUMERO DE PROCESOS Y SU IDENTIFICADOR DE CADA UNO DE ELLOS #####


# Prerequisitos para Windows:
# 1. Miniconda
#   Abrir miniconda y ejecutar:
#   conda install mpi4py numpy
# 2. Microsoft MPI

# Prerequisitos para Linux:
# En Ubuntu:
# apt install openmpi-bin libopenmpi-dev python3-mpi4py python3-numpy


# Ejecución en miniconda:
# mpiexec -n 2 python MPI01.py

# En Linux y MAC
# mpirun -n 2 python3 MPI01.py


##### MÓDULOS #####

# Módulo MPI para Python.
from mpi4py import MPI


##### INICIO #####

# Crea un objeto de tipo comunicador.
comm = MPI.COMM_WORLD

# Determina el identificador de un proceso.
rank = comm.Get_rank()

# Número de procesos.
size = comm.Get_size()

# Imprime Nº de procesos y el identificador de proceso.
print('Numero de procesos=%d, Id=%d' % (size, rank))
