from datetime import datetime

# Cadena de marca de tiempo Unix (como string)
timestamp_str = "1284105682"

# Convertir a entero
timestamp_int = int(timestamp_str)

# Convertir a datetime legible
fecha_legible = datetime.fromtimestamp(timestamp_int)

# Mostrar el resultado
print("INPUT Unix timestamp string:", timestamp_str)
print("OUTPUT:", fecha_legible.strftime("%Y-%m-%d %H:%M:%S"))
