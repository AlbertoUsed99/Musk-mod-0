from datetime import datetime

# Obtener fecha actual
hoy = datetime.now()

# Obtener el número de semana (ISO)
numero_semana = hoy.isocalendar()[1]

# Mostrar el número de la semana
print("Número de la semana:", numero_semana)
