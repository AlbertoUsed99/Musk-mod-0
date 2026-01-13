import os
def contar_lineas_historia():

    ruta_actual = os.getcwd()
    nombre_archivo = os.path.join("T1", "historia.txt")
    ruta_completa = os.path.join(ruta_actual, nombre_archivo)

    print(f"Directorio actual: {ruta_actual}")
    print("Buscando archivo:", nombre_archivo)
    print("Archivos en el directorio:", os.listdir(ruta_actual))

    try:
        with open(ruta_completa, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            print(f"El archivo contiene {len(lineas)} líneas.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró en:\n{ruta_actual}")
    except Exception as e:
        print("Ocurrió un error:", e)

contar_lineas_historia()
