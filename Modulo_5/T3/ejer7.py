import numpy as np

sampleArray = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])

# Caso 1: Ordenar por la segunda fila (reordenar columnas)
indices_fila = np.argsort(sampleArray[1, :])
sorted_by_second_row = sampleArray[:, indices_fila]

print("Ordenado por segunda fila (columnas reordenadas):")
print(sorted_by_second_row)

# Caso 2: Ordenar por la segunda columna (reordenar filas)
indices_columna = np.argsort(sampleArray[:, 1])
sorted_by_second_column = sampleArray[indices_columna, :]

print("\nOrdenado por segunda columna (filas reordenadas):")
print(sorted_by_second_column)
