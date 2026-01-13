import os
import pandas as pd

def kilometraje_medio_por_empresa():
    nombre_archivo = os.path.join("T2", "csvAutomobile_data.csv")
    ruta_completa = os.path.join(os.getcwd(), nombre_archivo)

    try:
        df = pd.read_csv(ruta_completa)

        # Detectar columnas relevantes
        columnas = df.columns.str.lower()
        if 'company' in columnas:
            columna_empresa = df.columns[columnas.tolist().index('company')]
        elif 'make' in columnas:
            columna_empresa = df.columns[columnas.tolist().index('make')]
        else:
            print("No se encontró una columna de empresa válida ('company' o 'make').")
            return

        if 'average-mileage' in columnas:
            columna_km = df.columns[columnas.tolist().index('average-mileage')]
        elif 'mileage' in columnas:
            columna_km = df.columns[columnas.tolist().index('mileage')]
        else:
            print("No se encontró una columna de kilometraje ('average-mileage' o 'mileage').")
            return

        # Convertir a numérico y eliminar errores
        df[columna_km] = pd.to_numeric(df[columna_km], errors='coerce')
        df = df.dropna(subset=[columna_km])

        # Calcular el promedio por empresa
        promedio_km = df.groupby(columna_empresa)[columna_km].mean().round(2)

        print("Kilometraje medio por empresa:")
        print(promedio_km)

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print("Ocurrió un error:", e)

kilometraje_medio_por_empresa()
