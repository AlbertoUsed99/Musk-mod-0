import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from estudiante import Estudiante  # Importamos la clase Estudiante desde estudiante.py

# Crear una instancia de la clase Estudiante
estudiante1 = Estudiante("Juan")

# Diccionario de meses con el número de asistencias
asistencias = {
    "Enero": 6,   # Modificado para pruebas
    "Febrero": 3, # Modificado para pruebas
    "Marzo": 8,
    "Abril": 7
}

# Usar el método público para evaluar las asistencias
resultado = estudiante1.evaluar_asistencias(asistencias)

# Imprimir el resultado
print(f"El resultado de evaluar las asistencias es: {resultado}")

# Llamar al método estático correctamente desde la clase
asignaturas_notas = {
    "Matemáticas": 3,
    "Historia": 6,
    "Ciencias": 4
}

Estudiante.imprimir_asignaturas_reprobadas(asignaturas_notas) 