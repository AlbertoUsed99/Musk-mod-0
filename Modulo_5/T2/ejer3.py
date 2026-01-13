import os
import pandas as pd

def coche_mas_caro():
    nombre_archivo = os.path.join("T2", "csvAutomobile_data.csv")
    ruta_actual = os.getcwd()
    ruta_completa = os.path.join(ruta_actual, nombre_archivo)

    try:
        df = pd.read_csv(ruta_completa)

        # Limpieza rápida para el precio: eliminar filas con precios no numéricos o faltantes
        df = df[pd.to_numeric(df['price'], errors='coerce').notnull()]
        df['price'] = df['price'].astype(float)

        # Encontrar fila con precio máximo
        idx_max = df['price'].idxmax()
        coche_mas_caro = df.loc[idx_max]

        # Suponiendo que la columna con el nombre de la empresa se llama 'company' o 'make'
        empresa = coche_mas_caro.get('company') or coche_mas_caro.get('make') or "Empresa desconocida"
        precio = coche_mas_caro['price']

        print(f"El coche más caro es de la empresa '{empresa}' con un precio de {precio}.")

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", e)

coche_mas_caro()
