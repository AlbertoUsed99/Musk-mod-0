from datetime import datetime, timedelta

# Obtener hora actual
hora_actual = datetime.now()

# Sumar 5 segundos
nueva_hora = hora_actual + timedelta(seconds=5)

# Mostrar resultados
print("Hora actual     :", hora_actual.strftime("%H:%M:%S"))
print("Hora +5 segundos:", nueva_hora.strftime("%H:%M:%S"))
