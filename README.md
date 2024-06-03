# Typewriter Simulation

Este programa en Python simula el efecto de una máquina de escribir al imprimir letras de frases específicas una por una en la consola. Cada carácter se imprime con un breve retraso, imitando el sonido y la visualización de una máquina de escribir. Este efecto se aplica no solo a cada carácter sino también entre las frases, donde se introduce un retraso más largo para simular el espacio entre las oraciones escritas.

## Como funciona

#### El script utiliza dos listas principales:

1. lines: Una lista de tuplas, donde cada tupla contiene una frase y el retraso asociado a cada carácter en esa frase.

2. delays: Una lista de tiempos de espera que determinan cuánto tiempo se espera antes de comenzar a escribir la siguiente frase.