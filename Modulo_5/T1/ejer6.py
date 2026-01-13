import os

def hash_display():
    nombre_archivo = os.path.join("T1", "materia.txt")
    ruta_actual = os.getcwd()
    ruta_completa = os.path.join(ruta_actual, nombre_archivo)

    print(f"Directorio actual: {ruta_actual}")
    print(f"Buscando archivo en: {nombre_archivo}")
    print("Archivos en el directorio:", os.listdir(ruta_actual))

    try:
        with open(ruta_completa, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            # Convertir todo a mayúsculas y separar cada carácter con '#'
            contenido_formateado = "#".join(contenido.upper())
            print(contenido_formateado)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró en:\n{ruta_actual}")
    except Exception as e:
        print("Ocurrió un error:", e)

hash_display()

