import numpy as np

# Crear un array de enteros sin signo de 16 bits (uint16), tamaño 4x2
array = np.array([[100, 200], [300, 400], [500, 600], [700, 800]], dtype=np.uint16)

# Imprimir los atributos solicitados
print("Array:")
print(array)
print("\nForma (shape):", array.shape)
print("Dimensiones (ndim):", array.ndim)
print("Tamaño de cada elemento (itemsize):", array.itemsize, "bytes")
