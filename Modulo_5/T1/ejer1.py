import os

def leer_poema():
    # Esto toma la carpeta donde está ESTE script:
    carpeta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_poema = os.path.join(carpeta_script, "poema.txt")
    
    try:
        with open(ruta_poema, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print(f"El archivo no existe en:\n {ruta_poema}")

if __name__ == "__main__":
    print("Leyendo desde:", os.path.abspath(__file__))
    leer_poema()
