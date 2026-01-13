import numpy as np

# Crear un array del 100 al 200 con paso de 10
datos = np.arange(100, 200, 10)

# Redimensionar a una matriz de 5 filas y 2 columnas
matriz = datos.reshape(5, 2)

# Mostrar la matriz
print("Matriz 5x2:")
print(matriz)
