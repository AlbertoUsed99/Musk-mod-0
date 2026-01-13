import os
from collections import Counter
import re

def frecuencia_palabras():
    nombre_archivo = os.path.join("T1", "story.txt")
    ruta_actual = os.getcwd()
    ruta_completa = os.path.join(ruta_actual, nombre_archivo)

    print(f"Directorio actual: {ruta_actual}")
    print(f"Buscando archivo en: {nombre_archivo}")
    print("Archivos en el directorio:", os.listdir(ruta_actual))

    try:
        with open(ruta_completa, "r", encoding="utf-8") as archivo:
            texto = archivo.read().lower()
            # Usar expresión regular para extraer palabras (sin puntuación)
            palabras = re.findall(r'\b\w+\b', texto)
            contador = Counter(palabras)

            print("Frecuencia de palabras:")
            for palabra, frecuencia in contador.most_common():
                print(f"{palabra}: {frecuencia}")

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró en:\n{ruta_actual}")
    except Exception as e:
        print("Ocurrió un error:", e)

frecuencia_palabras()
