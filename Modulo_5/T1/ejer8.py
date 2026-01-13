def añadir_y_mostrar_texto():
    nombre_archivo = "python.txt"
    texto_a_añadir = "Este es un texto añadido al archivo.\n"

    try:
        # Abrir en modo append (añadir), crea el archivo si no existe
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(texto_a_añadir)

        # Leer y mostrar el contenido completo
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)

    except Exception as e:
        print("Ocurrió un error:", e)

añadir_y_mostrar_texto()
