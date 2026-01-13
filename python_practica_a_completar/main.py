"""
main.py
Punto de entrada del proyecto Aeropuerto.

Lee los archivos de vuelos (TXT, CSV, JSON), los combina en un DataFrame,
y asigna slots a cada vuelo usando las clases Lector, Slot y Aeropuerto.
"""

import pandas as pd
from entities.lector import LectorCSV, LectorJSON, LectorTXT
from entities.aeropuerto import Aeropuerto


def cargar_datos(path: str) -> pd.DataFrame:
    """
    Detecta el tipo de archivo (CSV, JSON o TXT),
    lo lee con el lector correspondiente y devuelve un DataFrame limpio.
    """
    print(f"\n📂 Leyendo archivo: {path}")

    if path.endswith(".csv"):
        lector = LectorCSV(path)
    elif path.endswith(".json"):
        lector = LectorJSON(path)
    elif path.endswith(".txt"):
        lector = LectorTXT(path)
    else:
        raise ValueError(f"❌ Formato de archivo no soportado: {path}")

    # Leer archivo
    df = lector.lee_archivo()

    # Limpiar nombres de columnas
    df.columns = [col.strip() for col in df.columns]

    # Verificar columnas esperadas
    columnas_esperadas = ["id", "fecha_llegada", "retraso", "tipo_vuelo", "destino"]
    for col in columnas_esperadas:
        if col not in df.columns:
            raise ValueError(f"❌ Falta la columna '{col}' en el archivo {path}")

    # Convertir fechas (reemplazar 'T' si aparece)
    if df["fecha_llegada"].astype(str).str.contains("T").any():
        df["fecha_llegada"] = df["fecha_llegada"].str.replace("T", " ", regex=False)

    df["fecha_llegada"] = pd.to_datetime(
        df["fecha_llegada"], format="%d/%m/%Y %H:%M", errors="coerce"
    )

    return df


def main():
    print("=== 🛫 PROYECTO AEROPUERTO 🛬 ===")

    # 1️⃣ Cargar los tres archivos de vuelos
    rutas = [
        "data/vuelos_1.txt",
        "data/vuelos_2.csv",
        "data/vuelos_3.json"
    ]

    dataframes = []
    for ruta in rutas:
        try:
            df = cargar_datos(ruta)
            dataframes.append(df)
        except Exception as e:
            print(f"⚠️ Error al leer {ruta}: {e}")

    # 2️⃣ Combinar todos los vuelos en un solo DataFrame
    if not dataframes:
        print("❌ No se pudo cargar ningún archivo de vuelos.")
        return

    df_vuelos = pd.concat(dataframes, ignore_index=True)
    print("\n✅ Datos combinados correctamente.")
    print(df_vuelos.head())

    # 3️⃣ Crear el aeropuerto con los datos cargados
    aeropuerto = Aeropuerto(
        vuelos=df_vuelos,
        slots=10,                   # número de slots disponibles
        t_embarque_nat=30,          # tiempo de embarque nacional (min)
        t_embarque_internat=60      # tiempo de embarque internacional (min)
    )

    # 4️⃣ Asignar slots a los vuelos
    print("\n🛫 Asignando slots a los vuelos...")
    aeropuerto.asigna_slots()

    # 5️⃣ Mostrar resultado final
    print("\n=== RESULTADO FINAL ===")
    print(aeropuerto.df_vuelos)

    # 6️⃣ (Opcional) Guardar resultados en CSV
    salida = "data/vuelos_asignados.csv"
    aeropuerto.df_vuelos.to_csv(salida, index=False)
    print(f"\n📁 Resultados guardados en {salida}")


if __name__ == "__main__":
    main()
