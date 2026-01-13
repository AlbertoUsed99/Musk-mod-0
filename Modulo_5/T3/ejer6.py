import numpy as np

# Crear array con valores del 10 al 33 (24 números)
arr = np.arange(10, 34)[:24]

# Redimensionar a 8 filas y 3 columnas
matrix = arr.reshape(8, 3)

print("Matriz original:")
print(matrix)

