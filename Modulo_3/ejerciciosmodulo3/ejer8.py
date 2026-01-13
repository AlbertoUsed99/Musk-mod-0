import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from estudiante import Estudiante  # Importamos la clase Estudiante desde estudiante.py

# Crear una instancia de la clase Estudiante
estudiante1 = Estudiante("Juan")

# Calcular la media de una lista de notas
notas = [85, 90, 78, 92, 88]
estudiante1.calcular_media(notas)

# Imprimir el valor de grade
print(f"La media de {estudiante1.nombre} es: {estudiante1.grade}")

# Diccionario de asignaturas y sus respectivas notas
asignaturas_notas = {
    "Matemáticas": 4.5,
    "Física": 6.2,
    "Química": 3.9,
    "Historia": 5.5
}

# Usar el método estático para imprimir asignaturas con nota inferior a 5
Estudiante.imprimir_asignaturas_reprobadas(asignaturas_notas)