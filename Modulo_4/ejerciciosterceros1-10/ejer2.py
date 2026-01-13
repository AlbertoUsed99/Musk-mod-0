from datetime import datetime

# Cadena de entrada
entrada = "Jan 1 2014 2:43PM"

# Convertir la cadena a objeto datetime
formato_entrada = "%b %d %Y %I:%M%p"
fecha_convertida = datetime.strptime(entrada, formato_entrada)

# Mostrar el resultado en el formato deseado
print("OUTPUT:", fecha_convertida.strftime("%Y-%m-%d %H:%M:%S"))
