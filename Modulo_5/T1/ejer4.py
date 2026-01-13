import os

def buscar_el_en_notas():
    nombre_archivo = os.path.join("T1", "notas.txt")
    ruta_actual = os.getcwd()
    ruta_completa = os.path.join(ruta_actual, nombre_archivo)

    print(f"Directorio actual: {ruta_actual}")
    print(f"Buscando archivo en: {nombre_archivo}")
    print("Archivos en el directorio:", os.listdir(ruta_actual))

    try:
        with open(ruta_completa, "r", encoding="utf-8") as archivo:
            for num_linea, linea in enumerate(archivo, start=1):
                palabras = linea.lower().split()
                if "el" in palabras:
                    print(f"Línea {num_linea}: {linea.strip()}")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró en:\n{ruta_actual}")
    except Exception as e:
        print("Ocurrió un error:", e)

buscar_el_en_notas()
