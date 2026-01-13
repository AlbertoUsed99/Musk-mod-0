#1. Haz un programa que lea dos números a y b, y que escriba todos los números enteros a y b. Debe cumplirse que a < b. En caso que a > b, escribe los número de manera descendente.
# Leer los números a y b
a = int(input("Introduce el número a: "))
b = int(input("Introduce el número b: "))

# Comprobar si a es menor o mayor que b
if a < b:
    # Mostrar números en orden ascendente de a a b
    for numero in range(a, b + 1):
        print(numero, end=" ")
elif a > b:
    # Mostrar números en orden descendente de a a b
    for numero in range(a, b - 1, -1):
        print(numero, end=" ")
else:
    # Si a es igual a b, mostrar solo un número
    print(a)
#2. Haz un programa que lea una secuencia de 10 números y que escriba la media.
# Inicializar la suma de los números
suma = 0

# Leer 10 números
print("Introduce 10 números:")
for i in range(10):
    numero = float(input(f"Número {i+1}: "))
    suma += numero

# Calcular la media
media = suma / 10

# Mostrar la media
print(f"La media de los 10 números es: {media}")

#3. Haz un programa que dada una lista de naturales de tamaño n, indique la posición del primer número par.
# Leer la longitud de la lista
n = int(input("Introduce el tamaño de la lista (n): "))

# Leer la lista de números naturales
numeros = []
for i in range(n):
    numero = int(input(f"Introduce el número {i+1}: "))
    numeros.append(numero)

# Encontrar la posición del primer número par
posicion_par = -1  # Inicializamos con -1 para indicar que no se ha encontrado un número par
for i in range(n):
    if numeros[i] % 2 == 0:
        posicion_par = i
        break  # Salir del bucle al encontrar el primer número par

# Mostrar el resultado
if posicion_par != -1:
    print(f"El primer número par está en la posición {posicion_par + 1} (índice {posicion_par}).")
else:
    print("No se encontró ningún número par en la lista.")
#4. Haz un programa que lea un número n y que escriba la “tabla de multiplicar” de n.
# Leer el número n
n = int(input("Introduce un número para la tabla de multiplicar: "))

# Mostrar la tabla de multiplicar
print(f"Tabla de multiplicar del {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

#5. Haz un programa que lea un número y que lo escriba del revés.
# Leer un número
numero = input("Introduce un número: ")

# Escribir el número del revés
numero_reves = numero[::-1]
print(f"El número al revés es: {numero_reves}")

#6. Haz un programa que lea un número y que escriba el número de dígitos.
# Leer un número
numero = input("Introduce un número: ")

# Contar el número de dígitos
num_digitos = len(numero)
print(f"El número de dígitos es: {num_digitos}")

#7. Haz un programa que diga si un natural n es capicua o no.
# Leer un número natural
numero = input("Introduce un número natural: ")

# Verificar si es capicúa
if numero == numero[::-1]:
    print("El número es capicúa.")
else:
    print("El número no es capicúa.")

#8. Haz un programa que dada una secuencia de años acabada en 0 nos diga cuántos hay del siglo 20.
# Leer una secuencia de años acabada en 0
años = input("Introduce una secuencia de años acabada en 0 (separados por espacios): ").split()

# Contar cuántos años son del siglo 20
contador = 0
for año in años:
    if año.isdigit() and año.endswith('0'):
        if 1900 <= int(año) < 2000:
            contador += 1

print(f"Hay {contador} años del siglo 20 en la secuencia.")

#9. Haz un programa que reciba una secuencia de naturales de tamaño n y nos devuelva cuál es el primer natural que tiene un valor inferior al primer natural leído.
# Leer la cantidad de números a introducir
n = int(input("Introduce el tamaño de la secuencia: "))

# Leer la secuencia de números naturales
numeros = []
for i in range(n):
    numero = int(input(f"Introduce el número {i + 1}: "))
    numeros.append(numero)

# Encontrar el primer natural inferior al primer número leído
primer_numero = numeros[0]
primer_inferior = None

for numero in numeros[1:]:
    if numero < primer_numero:
        primer_inferior = numero
        break

if primer_inferior is not None:
    print(f"El primer natural que es inferior al primer número leído es: {primer_inferior}")
else:
    print("No hay ningún número inferior al primer número leído.")

#10. Haz un programa que cuente cuántos valores hay en una secuencia de enteros acabada en 0.
# Inicializar contador
contador = 0

# Leer una secuencia de enteros
print("Introduce una secuencia de enteros (termina con 0):")
while True:
    numero = int(input())
    if numero == 0:
        break
    contador += 1

print(f"Hay {contador} valores en la secuencia.")

#11. Haz un programa que devuelva el máximo de una secuencia de temperaturas acabada en 1000.
# Inicializar variable para el máximo
maximo = None

# Leer temperaturas
print("Introduce una secuencia de temperaturas (termina con 1000):")
while True:
    temperatura = float(input())
    if temperatura == 1000:
        break
    if maximo is None or temperatura > maximo:
        maximo = temperatura

if maximo is not None:
    print(f"La temperatura máxima es: {maximo}")
else:
    print("No se introdujeron temperaturas.")

#12. Haz un programa que dada una secuencia de valores acabada en 0 compruebe que ningún valor supera 50.
# Leer valores
print("Introduce una secuencia de valores (termina con 0):")
supera_50 = False

while True:
    valor = float(input())
    if valor == 0:
        break
    if valor > 50:
        supera_50 = True

if supera_50:
    print("Hay valores que superan 50.")
else:
    print("Ningún valor supera 50.")

#13. Haz un programa que dada una secuencia de valores acabada en 0 compruebe que ningún valor supera 50 y que no hay más de tres que superen 40.
# Leer valores
print("Introduce una secuencia de valores (termina con 0):")
contador_supera_40 = 0
supera_50 = False

while True:
    valor = float(input())
    if valor == 0:
        break
    if valor > 50:
        supera_50 = True
    if valor > 40:
        contador_supera_40 += 1

if supera_50:
    print("Hay valores que superan 50.")
elif contador_supera_40 > 3:
    print("Hay más de tres valores que superan 40.")
else:
    print("Todos los valores están dentro de los límites permitidos.")

#14. Haz un programa que dada una secuencia de valores acabada en 0 diga si hay más positivos o negativos.
# Leer valores
print("Introduce una secuencia de valores (termina con 0):")
contador_positivos = 0
contador_negativos = 0

while True:
    valor = int(input())
    if valor == 0:
        break
    if valor > 0:
        contador_positivos += 1
    elif valor < 0:
        contador_negativos += 1

if contador_positivos > contador_negativos:
    print("Hay más positivos que negativos.")
elif contador_negativos > contador_positivos:
    print("Hay más negativos que positivos.")
else:
    print("Hay el mismo número de positivos y negativos.")

#15. Haz un programa que dada una secuencia de valores enteros acabada en 0 diga cuál es el número que hay antes de primer negativo encontrado.
# Leer valores
print("Introduce una secuencia de valores (termina con 0):")
ultimo_valor = None

while True:
    valor = int(input())
    if valor == 0:
        break
    if valor < 0:
        if ultimo_valor is not None:
            print(f"El número antes del primer negativo encontrado es: {ultimo_valor}")
        else:
            print("No se encontró ningún número antes del primer negativo.")
        break
    ultimo_valor = valor

#16. Haz un programa que dada una secuencia de valores enteros acabada en 0 diga cuántos son múltiples del primero.
# Leer valores
print("Introduce una secuencia de valores (termina con 0):")
primer_valor = None
contador_multiplos = 0

while True:
    valor = int(input())
    if valor == 0:
        break
    if primer_valor is None:
        primer_valor = valor
    elif valor % primer_valor == 0:
        contador_multiplos += 1

if primer_valor is not None:
    print(f"El número de valores que son múltiplos de {primer_valor} es: {contador_multiplos}")
else:
    print("No se introdujeron valores.")

#17. Haz un programa que lea varias descripciones de rectángulos y de círculos, y que para cada una escriba el área correspondiente. La entrada empieza con un número n, seguido de n descripciones. Si es de un rectángulo, se tiene la palabra “rectángulo” 
# seguida de dos reales estrictamente positivos que indican la longitud y la anchura. Si es de un círculo, se tiene la palabra “círculo” seguida de un real estrictamente positivo que indica el radio.
import math

# Leer el número de descripciones
n = int(input("Introduce el número de descripciones: "))

# Procesar cada descripción
for _ in range(n):
    descripcion = input("Introduce la descripción (rectángulo o círculo): ").strip().lower().split()
    
    if descripcion[0] == "rectángulo":
        longitud = float(descripcion[1])
        anchura = float(descripcion[2])
        area = longitud * anchura
        print(f"Área del rectángulo: {area:.2f}")
    elif descripcion[0] == "círculo":
        radio = float(descripcion[1])
        area = math.pi * radio ** 2
        print(f"Área del círculo: {area:.2f}")
    else:
        print("Descripción no válida.")
