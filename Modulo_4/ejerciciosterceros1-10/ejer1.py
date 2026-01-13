from datetime import datetime

# Obtener fecha y hora actual
ahora = datetime.now()

print("a) Fecha y hora actuales:", ahora)
print("b) Año actual:", ahora.strftime("%Y"))
print("c) Mes del año:", ahora.strftime("%B"))
print("d) Número de la semana del año:", ahora.strftime("%U"))
print("e) Día de la semana (número):", ahora.strftime("%w"))
print("f) Día del año:", ahora.strftime("%j"))
print("g) Día del mes:", ahora.strftime("%d"))
print("h) Día de la semana (nombre):", ahora.strftime("%A"))
