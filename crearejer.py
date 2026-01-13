import os

# Nombre de la carpeta
folder_name = "T3"

# Crear la carpeta si no existe
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Crear los archivos ejer4.py a ejer9.py dentro de la carpeta T3
for i in range(4, 10):
    file_path = os.path.join(folder_name, f"ejer{i}.py")
    with open(file_path, 'w') as f:
        # Opcional: escribir un comentario inicial en cada archivo
        f.write(f"# Archivo {file_path}\n")
