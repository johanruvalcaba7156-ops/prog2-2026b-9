'''Funciones de interaccion con el sistema'''

import os
import time

sistema = os.name # Obtiene el sistema operativo del equipo donde se ejecuta el programa

def limpiar():
    '''Limpia la pantalla de la terminal'''

    os.system('cls' if sistema == 'nt' else 'clear') # Limpia la pantalla dependiendo del sistema operativo

def esperar():
    '''Agrega tiempo de espera para que el usuario pueda leer los mensajes en pantalla'''

    print("\nValidando informacion, espere un momento...")
    time.sleep(2) # Agrega un tiempo de espera de 2 segundos
    limpiar() # Limpia la pantalla despues de la espera
