import sys
# Importamos la funcion sleep del moduko time, que se usa para pausar la ejecucion del programa durante el numero de segundos especificado. 
from time import sleep
import time 


def sign_of_the_times(): 
    # Esta tupla contiene una linea de texto y un retraso en segundos que se aplicara despues de imprimir cada caracter. 
    lines = [
        ("We don't talk enough", 0.15),
        ("We should open up", 0.15),
        ("Before it's all too much", 0.12),
        ("Will we ever learn?", 0.16),
        ("We've been here before", 0.15),
        ("It's just what we know", 0.12),
        ("Stop your crying, baby", 0.09),
        ("It's a sign of the times", 0.07), 
        ("We gotta get away", 0.09),
        ("We got to get away", 0.09),
        ("We got to get away...", 0.09) ]

    # Es lista es de retrasos, donde cada elemento es un numero que representa el timepo en segundos que el programa esperara despues de imprimir cada linea.
    delays = [1, 1.4, 4, 1.9, 0.8, 5, 0.4, 2.4, 2, 2, 1]

    for i, (line, char_delay) in enumerate(lines): 
        for char in line: 
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        # Despues de ipirmir cada linea, el programa esperara durante un numero de segundos que se especifica en la lista delays.
        time.sleep(delays[i])
        print("")
        

sign_of_the_times()