# ejer7.py
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from estudiante import Estudiante  # Importamos la clase Estudiante desde estudiante.py

# Crear una instancia de la clase
estudiante1 = Estudiante("Juan")

# Calcular la media de una lista de notas
notas = [85, 90, 78, 92, 88]
estudiante1.calcular_media(notas)

# Imprimir el valor de grade
print(f"La media de {estudiante1.nombre} es: {estudiante1.grade}")
