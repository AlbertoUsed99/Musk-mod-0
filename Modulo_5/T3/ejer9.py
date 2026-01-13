import numpy as np

sampleArray = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])

newColumn = np.array([[10, 10, 10]]).T  # Transpuesta para que sea columna (3x1)

# Eliminar la segunda columna (índice 1)
array_sin_segunda_col = np.delete(sampleArray, 1, axis=1)

# Insertar la nueva columna en la posición 1
result = np.insert(array_sin_segunda_col, 1, newColumn.flatten(), axis=1)

print("Matriz resultante:")
print(result)

