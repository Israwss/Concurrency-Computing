##### INICIA 3 HILOS, IMPRIME INFORMACON DE SU INICIO Y FINALIZACION #####
##### ESPERA HASTA QUE EL ULTIMO HILO TERMINE PARA CONTINUAR         #####


import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(5)
    logging.info("Thread %s: finishing", name)


##### INICIO #####

if __name__ == "__main__":

    # Formato de impresón
    
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    # Lista vacía para colocar los objetos tipo hilo.
    hilos = list()


    # Crea los hilos y los inicializa.

    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        hilos.append(x)
        x.start()
        

    # Detiene el hilo principal hasta que el último hilo termine.
    # Se puede comentar este bloque para ver el efecto de 'join()'.

    for index, hilo in enumerate(hilos):
        logging.info("Main    : before joining thread %d.", index)
        hilo.join()
        logging.info("Main    : thread %d done", index)

# Obtiene el número de hilos activos.
print("Main: Número de hilos activos al final: ", threading.active_count())
