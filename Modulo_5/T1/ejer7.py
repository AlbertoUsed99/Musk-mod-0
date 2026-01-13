import string
import os

def generar_archivos_letras():
    carpeta = "T1"  # Puedes cambiar o quitar esta línea si quieres crear en otro lugar
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    for letra in string.ascii_uppercase:  # Genera letras de la A a la Z
        nombre_archivo = f"{letra}.txt"
        ruta_archivo = os.path.join(carpeta, nombre_archivo)
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(f"Este es el archivo {nombre_archivo}\n")
        print(f"Archivo creado: {ruta_archivo}")

generar_archivos_letras()
