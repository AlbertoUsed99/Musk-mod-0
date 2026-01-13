import os

def comprobar_existencia_archivo():
    nombre_archivo = os.path.join("T1", "materia.txt")  # archivo dentro de T1
    ruta_actual = os.getcwd()  # directorio donde se ejecuta el script
    ruta_completa = os.path.join(ruta_actual, nombre_archivo)

    print(f"Directorio actual: {ruta_actual}")
    print(f"Buscando archivo en: {ruta_completa}")
    print(f"Archivos en el directorio actual: {os.listdir(ruta_actual)}")

    if not os.path.exists(os.path.join(ruta_actual, "T1")):
        print("La carpeta 'T1' NO existe dentro del directorio actual.")
        return

    archivos_en_T1 = os.listdir(os.path.join(ruta_actual, "T1"))
    print(f"Archivos en la carpeta 'T1': {archivos_en_T1}")

    if os.path.isfile(ruta_completa):
        print(f"El archivo '{nombre_archivo}' existe.")
    else:
        print(f"El archivo '{nombre_archivo}' NO existe.")

comprobar_existencia_archivo()
