#1. Haz un programa que cree una función en Python que dada una secuencia devuelva únicamente los números pares.
def obtener_pares(secuencia):
    # Filtrar y devolver solo los números pares
    return [numero for numero in secuencia if numero % 2 == 0]

# Ejemplo de uso
secuencia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = obtener_pares(secuencia)
print(pares)

#2. Haz un programa que cree una función con longitud variable de argumentos.
def sumar_todos_los_argumentos(*args):
    # Sumar todos los argumentos pasados a la función
    return sum(args)

# Ejemplo de uso
resultado = sumar_todos_los_argumentos(1, 2, 3, 4, 5)
print(f'La suma es: {resultado}')

#3. Haz un programa que devuelva múltiples valores desde una función.

#Crea la función calculaion() de modo que pueda aceptar dos variables y calcular sumas y restas. Además, debe devolver tanto la suma como la resta en una sola llamada.
def calculo(a, b):
    # Calcular la suma y la resta
    suma = a + b
    resta = a - b
    # Devolver ambos valores
    return suma, resta

# Ejemplo de uso
numero1 = 10
numero2 = 5

suma, resta = calculo(numero1, numero2)
print(f'La suma es: {suma}')
print(f'La resta es: {resta}')

#4. Haz un programa que cree una función con un argumento por defecto.
    #Crea una función show_employee() usando las siguientes condiciones.

    #-Debe aceptar el nombre y el salario del empleado y mostrar ambos.

    #-Si falta el salario en la llamada de función, asigne el valor predeterminado 9000 al salario.
def show_employee(nombre, salario=9000):
    # Mostrar el nombre y el salario del empleado
    print(f'Nombre: {nombre}, Salario: {salario}')

# Ejemplo de uso con salario especificado
show_employee("Juan", 12000)

# Ejemplo de uso sin especificar salario (se usa el valor predeterminado)
show_employee("Ana")

#5. Haz un programa que cree una función interna para calcular la suma de la siguiente manera: Crea una función externa que acepte dos parámetros, a y b. Crea una función interna dentro de una función externa que calculará la suma de a y b. Por último, una función externa que sumará 5 en la suma y la devolverá.
def funcion_externa(a, b):
    # Función interna que calcula la suma de a y b
    def funcion_interna(x, y):
        return x + y
    
    # Calcular la suma usando la función interna
    suma = funcion_interna(a, b)
    
    # Añadir 5 a la suma y devolver el resultado final
    suma_con_5 = suma + 5
    return suma_con_5

# Ejemplo de uso
resultado = funcion_externa(3, 7)
print(f'El resultado final es: {resultado}')

#6. Haz un que cree una función que escriba el cuadrado y la raíz cuadrada de una secuencia de naturales.
import math

def calcular_cuadrados_y_raices(secuencia):
    resultado = []
    for numero in secuencia:
        cuadrado = numero ** 2
        raiz_cuadrada = math.sqrt(numero)
        resultado.append((numero, cuadrado, raiz_cuadrada))
    return resultado

# Ejemplo de uso
secuencia = [1, 2, 3, 4, 5, 6]
resultado = calcular_cuadrados_y_raices(secuencia)

# Imprimir los resultados
for numero, cuadrado, raiz in resultado:
    print(f'Número: {numero}, Cuadrado: {cuadrado}, Raíz cuadrada: {raiz:.2f}')

#7. Haz un programa que cree una función que deje a, b y c ordenados de pequeño a grande. Por ejemplo, si a =7, b = −3 y c = 1, los valores después de la llamada deben ser a =−3, b = 1 y c = 7.
def ordenar_valores(a, b, c):
    # Ordenar los valores de menor a mayor
    a, b, c = sorted([a, b, c])
    return a, b, c

# Ejemplo de uso
a, b, c = 7, -3, 1
a, b, c = ordenar_valores(a, b, c)

# Imprimir los valores ordenados
print(f'a = {a}, b = {b}, c = {c}')
