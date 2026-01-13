import random

def generador_aleatorios(n):
    for _ in range(n):
        yield random.random()

# Ejemplo de uso
for numero in generador_aleatorios(5):
    print(numero)
