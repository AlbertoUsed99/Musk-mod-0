import os

def display_words():
    nombre_archivo = os.path.join("T1", "story.txt")
    ruta_actual = os.getcwd()
    ruta_completa = os.path.join(ruta_actual, nombre_archivo)

    print(f"Directorio actual: {ruta_actual}")
    print(f"Buscando archivo en: {nombre_archivo}")
    print("Archivos en el directorio:", os.listdir(ruta_actual))

    try:
        with open(ruta_completa, "r", encoding="utf-8") as archivo:
            for num_linea, linea in enumerate(archivo, start=1):
                palabras = linea.split()
                # Filtrar palabras con menos de 4 caracteres
                palabras_cortas = [palabra for palabra in palabras if len(palabra) < 4]
                if palabras_cortas:
                    print(f"Línea {num_linea}: {' '.join(palabras_cortas)}")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró en:\n{ruta_actual}")
    except Exception as e:
        print("Ocurrió un error:", e)

display_words()
