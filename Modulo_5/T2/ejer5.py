import os
import pandas as pd

def contar_coches_por_empresa():
    nombre_archivo = os.path.join("T2", "csvAutomobile_data.csv")
    ruta_completa = os.path.join(os.getcwd(), nombre_archivo)

    try:
        df = pd.read_csv(ruta_completa)

        # Detectar la columna que representa la empresa
        columnas = df.columns.str.lower()
        if 'company' in columnas:
            columna_empresa = df.columns[columnas.tolist().index('company')]
        elif 'make' in columnas:
            columna_empresa = df.columns[columnas.tolist().index('make')]
        else:
            print("No se encontró una columna de empresa válida ('company' o 'make').")
            return

        # Contar coches por empresa
        conteo = df[columna_empresa].value_counts()

        print("Total de coches por empresa:")
        print(conteo)

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", e)

contar_coches_por_empresa()
