import os
import pandas as pd
import numpy as np

def limpiar_csv():
    nombre_archivo = os.path.join("T2", "csvAutomobile_data.csv")
    ruta_actual = os.getcwd()
    ruta_completa = os.path.join(ruta_actual, nombre_archivo)
    archivo_limpio = os.path.join(ruta_actual, "T2", "csvAutomobile_data_limpio.csv")

    try:
        # Leer CSV
        df = pd.read_csv(ruta_completa)

        # Reemplazar "?", "n.a" y valores NaN en todo el DataFrame
        df.replace(["?", "n.a"], np.nan, inplace=True)  # Convertimos esos valores a NaN
        df.fillna("", inplace=True)  # Luego reemplazamos NaN por cadena vacía (puedes cambiarlo)

        # Guardar archivo limpio
        df.to_csv(archivo_limpio, index=False)
        print(f"Archivo limpio guardado en: {archivo_limpio}")

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", e)

limpiar_csv()
