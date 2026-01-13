from datetime import datetime, timedelta

# Fecha de inicio (puedes cambiarla según lo que necesites)
fecha_inicial = datetime(2025, 1, 1)

# Número de fechas y días de diferencia
cantidad_fechas = 12
dias_diferencia = 20

# Generar las fechas
fechas = [fecha_inicial + timedelta(days=dias_diferencia * i) for i in range(cantidad_fechas)]

# Mostrar resultados
for i, fecha in enumerate(fechas, 1):
    print(f"Fecha {i}: {fecha.strftime('%Y-%m-%d')}")
