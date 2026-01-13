#1. Haz un programa que lea dos palabras y que indique el orden lexicográfico. Escribe en una línea indicando si a < b, a > b o a = b. Ejemplo: a = Anna, b = Javier, Anna < Javier.
# Leer dos palabras del usuario
a = input("Ingrese la primera palabra (a): ")
b = input("Ingrese la segunda palabra (b): ")

# Comparar las palabras y mostrar el resultado
if a < b:
    print(f"{a} < {b}")
elif a > b:
    print(f"{a} > {b}")
else:
    print(f"{a} = {b}")
    
#2. Haz un programa que lea una letra y que indique por pantalla si es una mayúscula, si es una minúscula, si es una vocal, y si es una consonante.
# Leer una letra del usuario
letra = input("Ingrese una letra: ")

# Verificar que se haya ingresado solo una letra
if len(letra) != 1 or not letra.isalpha():
    print("Por favor, ingrese solo una letra.")
else:
    # Verificar si la letra es mayúscula o minúscula
    if letra.isupper():
        tipo_caso = "mayúscula"
    else:
        tipo_caso = "minúscula"
    
    # Verificar si es vocal o consonante
    if letra.lower() in 'aeiou':
        tipo_letra = "vocal"
    else:
        tipo_letra = "consonante"

    # Mostrar resultados
    print(f"La letra '{letra}' es {tipo_caso} y es una {tipo_letra}.")

#3.Haz un programa que lea un entero que representa una temperatura en grados Celsius, y 
# que diga si hace calor, si hace frío, o si se está bien. Suponed que hace calor si la temperatura es más alta que 30 grados,
#  que hace frío si es más baja que 10 grados, y que se está bien en otro caso.

# Función que determina la sensación térmica según la temperatura
def determinar_sensacion(temperatura):
    if temperatura > 30:
        return "Hace calor."
    elif temperatura < 10:
        return "Hace frío."
    else:
        return "Se está bien."

# Leer la temperatura como un número entero
temperatura = int(input("Introduce la temperatura en grados Celsius: "))

# Mostrar el resultado
resultado = determinar_sensacion(temperatura)
print(resultado)


#4. Haz un programa que, dados dos intervalos, calcule el intervalo correspondiente a la intersección o indique que esta es vacía.

# Función para calcular la intersección de dos intervalos
def calcular_interseccion(intervalo1, intervalo2):
    # Obtenemos los límites de los intervalos
    inicio1, fin1 = intervalo1
    inicio2, fin2 = intervalo2
    
    # Calculamos el inicio y el fin del intervalo de intersección
    inicio_interseccion = max(inicio1, inicio2)
    fin_interseccion = min(fin1, fin2)
    
    # Verificamos si hay intersección
    if inicio_interseccion <= fin_interseccion:
        return (inicio_interseccion, fin_interseccion)
    else:
        return None  # Intersección vacía

# Leer los dos intervalos
inicio1 = int(input("Introduce el inicio del primer intervalo: "))
fin1 = int(input("Introduce el fin del primer intervalo: "))
inicio2 = int(input("Introduce el inicio del segundo intervalo: "))
fin2 = int(input("Introduce el fin del segundo intervalo: "))

# Calcular la intersección
intervalo1 = (inicio1, fin1)
intervalo2 = (inicio2, fin2)
interseccion = calcular_interseccion(intervalo1, intervalo2)

# Mostrar el resultado
if interseccion:
    print(f"La intersección de los intervalos es: {interseccion}")
else:
    print("La intersección es vacía.")

#5. Haz un programa que indique si un año es bisiesto o no. Un año bisiesto tiene 366 días. Después de la reforma gregoriana, los años bisiestos son los múltiplos de cuatro que no acaban en dos ceros, 
# y también los acabados en dos ceros tales que el número que queda después de sacar los dos ceros finales es divisible por cuatro. Así, 1800 y 1900, a pesar de ser múltiples de cuatro, no fueran bisiestos; en cambio, 2000 lo fue.

# Función para determinar si un año es bisiesto
def es_bisiesto(ano):
    # Verificamos si es divisible por 400 (años acabados en dos ceros y divisibles por 400)
    if ano % 400 == 0:
        return True
    # Verificamos si es divisible por 100 (años acabados en dos ceros pero no divisibles por 400)
    if ano % 100 == 0:
        return False
    # Verificamos si es divisible por 4 (años bisiestos comunes)
    if ano % 4 == 0:
        return True
    # No es bisiesto
    return False

# Leer el año
ano = int(input("Introduce un año: "))

# Comprobar si es bisiesto
if es_bisiesto(ano):
    print(f"El año {ano} es bisiesto.")
else:
    print(f"El año {ano} no es bisiesto.")

#6. Haz un programa que añada un segundo en una hora del día, dadas sus horas, minutos y segundos.
# Función para añadir un segundo a la hora dada
def anadir_segundo(horas, minutos, segundos):
    # Añadir un segundo
    segundos += 1

    # Ajustar los segundos si son 60
    if segundos == 60:
        segundos = 0
        minutos += 1

    # Ajustar los minutos si son 60
    if minutos == 60:
        minutos = 0
        horas += 1

    # Ajustar las horas si son 24
    if horas == 24:
        horas = 0

    return horas, minutos, segundos

# Leer la hora actual
horas = int(input("Introduce las horas (0-23): "))
minutos = int(input("Introduce los minutos (0-59): "))
segundos = int(input("Introduce los segundos (0-59): "))

# Añadir un segundo
nuevas_horas, nuevos_minutos, nuevos_segundos = anadir_segundo(horas, minutos, segundos)

# Mostrar la nueva hora
print(f"La nueva hora es: {nuevas_horas:02}:{nuevos_minutos:02}:{nuevos_segundos:02}")

#7. Haz un programa que lea un real x≥0 y que escriba ⌊x⌋ (la parte entera inferior de x), ⌈x⌉ (la parte entera superior de x), y el redondeo de x.
# Leer un número real x ≥ 0
x = float(input("Introduce un número real x (x ≥ 0): "))

# Parte entera inferior (⌊x⌋)
parte_entera_inferior = int(x)  # Truncamos la parte decimal para obtener la parte entera inferior

# Parte entera superior (⌈x⌉)
if x == int(x):
    parte_entera_superior = int(x)
else:
    parte_entera_superior = int(x) + 1

# Redondeo de x
if (x - int(x)) < 0.5:
    redondeo = int(x)
else:
    redondeo = int(x) + 1

# Mostrar los resultados
print(f"Parte entera inferior (⌊x⌋): {parte_entera_inferior}")
print(f"Parte entera superior (⌈x⌉): {parte_entera_superior}")
print(f"Redondeo de x: {redondeo}")
