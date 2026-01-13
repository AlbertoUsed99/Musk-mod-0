import numpy as np

sampleArray = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])

# Máximo por columnas (eje 0)
max_axis0 = np.max(sampleArray, axis=0)

# Mínimo por filas (eje 1)
min_axis1 = np.min(sampleArray, axis=1)

print("Máximo a lo largo del eje 0 (columnas):", max_axis0)
print("Mínimo a lo largo del eje 1 (filas):", min_axis1)
