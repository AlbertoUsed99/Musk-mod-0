import os
import pandas as pd

def coche_mas_caro_por_empresa():
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

        # Asegurarse de que los precios sean numéricos
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df = df.dropna(subset=['price'])

        # Obtener el coche más caro por empresa
        coches_mas_caros = df.loc[df.groupby(columna_empresa)['price'].idxmax()]

        print("Coche más caro por empresa:")
        print(coches_mas_caros[[columna_empresa, 'price']])

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", e)

coche_mas_caro_por_empresa()
