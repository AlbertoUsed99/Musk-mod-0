import os
import pandas as pd

def ordenar_coches_por_precio():
    nombre_archivo = os.path.join("T2", "csvAutomobile_data.csv")
    ruta_completa = os.path.join(os.getcwd(), nombre_archivo)

    try:
        df = pd.read_csv(ruta_completa)

        # Asegurarse de que la columna 'price' sea numérica
        df['price'] = pd.to_numeric(df['price'], errors='coerce')

        # Eliminar filas sin precio válido
        df = df.dropna(subset=['price'])

        # Ordenar por precio ascendente
        df_ordenado = df.sort_values(by='price', ascending=True)

        print("Coches ordenados por precio (de menor a mayor):")
        print(df_ordenado)

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", e)

ordenar_coches_por_precio()
