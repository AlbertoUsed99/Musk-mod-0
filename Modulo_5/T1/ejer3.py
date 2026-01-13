import os

def contar_palabras_historia():
    nombre_archivo = os.path.join("T1", "historia.txt")
    ruta_actual = os.getcwd()
    ruta_completa = os.path.join(ruta_actual, nombre_archivo)

    print(f"Directorio actual: {ruta_actual}")
    print(f"Buscando archivo en: {nombre_archivo}")
    print("Archivos en el directorio:", os.listdir(ruta_actual))

    try:
        with open(ruta_completa, "r", encoding="utf-8") as archivo:
            total_palabras = 0
            for linea in archivo:
                palabras = linea.split()
                total_palabras += len(palabras)
            print(f"El archivo contiene un total de {total_palabras} palabras.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró en:\n{ruta_actual}")
    except Exception as e:
        print("Ocurrió un error:", e)

contar_palabras_historia()
