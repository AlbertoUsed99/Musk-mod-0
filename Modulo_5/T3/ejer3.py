import numpy as np

# Array de muestra
sampleArray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

# Tomar la tercera columna (índice 2)
tercera_columna = sampleArray[:, 2]

# Mostrar el resultado
print("Tercera columna de todas las filas:")
print(tercera_columna)
