import os
import pandas as pd

def mostrar_primeras_ultimas_filas():
    nombre_archivo = os.path.join("T2", "csvAutomobile_data.csv")
    ruta_actual = os.getcwd()
    ruta_completa = os.path.join(ruta_actual, nombre_archivo)

    print(f"Directorio actual: {ruta_actual}")
    print(f"Buscando archivo en: {nombre_archivo}")

    try:
        df = pd.read_csv(ruta_completa)
        print("Cinco primeras filas:")
        print(df.head(5))
        print("\nCinco últimas filas:")
        print(df.tail(5))

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", e)

mostrar_primeras_ultimas_filas()
