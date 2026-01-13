import os
import pandas as pd

def mostrar_coches_toyota():
    nombre_archivo = os.path.join("T2", "csvAutomobile_data.csv")
    ruta_completa = os.path.join(os.getcwd(), nombre_archivo)

    try:
        df = pd.read_csv(ruta_completa)

        # Normalizamos posibles nombres de columna
        columnas = df.columns.str.lower()
        if 'company' in columnas:
            columna_empresa = df.columns[columnas.tolist().index('company')]
        elif 'make' in columnas:
            columna_empresa = df.columns[columnas.tolist().index('make')]
        else:
            print("No se encontró una columna de empresa válida ('company' o 'make').")
            return

        # Filtrar los coches cuya empresa sea 'toyota'
        toyota_cars = df[df[columna_empresa].str.lower() == "toyota"]

        if toyota_cars.empty:
            print("No se encontraron coches Toyota en el archivo.")
        else:
            print("Datos de los coches Toyota:")
            print(toyota_cars)

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", e)

mostrar_coches_toyota()
