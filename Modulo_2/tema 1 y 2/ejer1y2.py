#1. Haz un programa que escriba una línea con el mensaje “Buenos días a todo el mundo!”.
print('Buenos dias a todo el mundo!')

#2. Haz un programa que declare tres palabras a, b y c, y que escriba una línea con c, b y a en este orden.
# Declarar las palabras en una lista
palabras = ["Python", "es", "genial"]

# Imprimir las palabras en el orden c, b, a
print(palabras[2], palabras[1], palabras[0])  # c, b, a

#3. Haz un programa que declare dos números y que escriba la suma.
# Declarar los números en una lista
numeros = [10, 5]

# Calcular la suma
suma = sum(numeros)

# Imprimir la suma
print("La suma de", numeros[0], "y", numeros[1], "es:", suma)

#4. Haz un programa que declare dos números y que escriba el máximo.
x = 10
y = 41

print(max(x, y))

#5. Haz un programa que declare tres números, todos diferentes, y que escriba el máximo.
numeros = [10, 25, 15]

# Encontrar el máximo
maximo = max(numeros)

# Imprimir el máximo
print("El número máximo entre", numeros[0], ",", numeros[1], "y", numeros[2], "es:", maximo)

#6. Hacer un programa que dado un valor calcule su cuadrado y el cubo. 
x = 10

# Calcular el cuadrado y el cubo usando la función pow()
cuadrado = pow(x, 2)  # Calcula el cuadrado
cubo = pow(x, 3)      # Calcula el cubo

# Imprimir los resultados
print("El cuadrado de", x, "es:", cuadrado)
print("El cubo de", x, "es:", cubo)

#7. Haz un programa que devuelva el valor absoluto de un número.
def valor_absoluto(numero):
    return abs(numero)

# Declarar un número
x = -10

# Obtener el valor absoluto
resultado = valor_absoluto(x)

# Imprimir el resultado
print("El valor absoluto de", x, "es:", resultado)

#8. Haz un programa que lea dos naturales a y b, con b > 0, y que escriba la división entera d y el residuo r de a entre b. 
# Recordad que, por definición, d y r tienen que ser los únicos enteros tales que 0 ≤ r < b y d · b + r = a. Ejemplo: a=32, b=5, d=6, r=2 ya que 32 = 5 * 6 + 2
def calcular_division(a, b):
    residuo = a % b
    cuociente_entero = a // b
    return residuo, cuociente_entero

# Leer los números
a = 32
b = 5

# Calcular el residuo y la división entera
residuo, cuociente_entero = calcular_division(a, b)

# Imprimir los resultados
print(f'Dividendo: {a}, Divisor: {b}, Residuo: {residuo}, Cuociente: {cuociente_entero}')

#9. Haz un programa que, dada una cantidad de segundos, diga cuántas horas, minutos y segundos representa.
def calcular_tiempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return horas, minutos, segundos_restantes

# Usar la función
x = 3661
horas, minutos, segundos = calcular_tiempo(x)

# Imprimir los resultados
print(f'{x} segundos son {horas} horas, {minutos} minutos y {segundos} segundos')

#10. Haz un programa que dada una temperatura en grados Celsius la muestre en grados Fahrenheit y en grados Kelvin. (F= 1.8C + 32 y  ºK =°C + 273ºK).
c = 40
f = 1.8 * c + 32
k = c + 273

print('Temperatura en Celsius: {}'.format(c))
print('Temperatura en Fahrenheit: {}'.format(f))
print('Temperatura en Kelvin: {}'.format(k))
