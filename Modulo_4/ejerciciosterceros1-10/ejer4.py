from datetime import datetime, timedelta

# Obtener la fecha actual
fecha_actual = datetime.now()

# Restar 5 días
nueva_fecha = fecha_actual - timedelta(days=5)

# Mostrar el resultado
print("Fecha actual:", fecha_actual.strftime("%Y-%m-%d"))
print("Fecha menos 5 días:", nueva_fecha.strftime("%Y-%m-%d"))
