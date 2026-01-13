import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from jet import Jet  # Importar la clase desde jet.py

# Crear instancias de la clase Jet con la cantidad
f14 = Jet("F14", "USA", 87)
mirage2000 = Jet("Mirage2000", "France", 35)

# Imprimir atributos de cada instancia
print(f"{f14.name}: {f14.origin}, Cantidad: {f14.cantidad}")
print(f"{mirage2000.name}: {mirage2000.origin}, Cantidad: {mirage2000.cantidad}")
