import numpy as np

arrayone = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])

# Sumar las matrices
result = arrayone + arrayTwo

# Elevar al cuadrado cada elemento de la matriz resultante
result_squared = result ** 2

print("Matriz suma:")
print(result)
print("\nMatriz con elementos al cuadrado:")
print(result_squared)
