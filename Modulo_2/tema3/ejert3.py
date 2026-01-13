#1. Haz un programa que lea un número decimal por pantalla, lo convierta a entero y lo imprima.
# Leer un número decimal del usuario
numero_decimal = float(input("Ingresa un número decimal: "))

# Convertir el número decimal a entero
numero_entero = int(numero_decimal)

# Imprimir el resultado
print(f'El número decimal {numero_decimal} convertido a entero es: {numero_entero}')

#2. Haz un programa que lea un número decimal por pantalla e imprima su tipo y su valor redondeado en la misma línea.
# Leer un número decimal del usuario
numero_decimal = float(input("Ingresa un número decimal: "))

# Redondear el número
numero_redondeado = round(numero_decimal)

# Imprimir el tipo y el valor redondeado
print(f'Tipo: {type(numero_decimal)}, Valor redondeado: {numero_redondeado}')

#3. Haz un programa que lea dos números por pantalla e imprima su diferencia en valor absoluto.
# Leer dos números del usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Calcular la diferencia en valor absoluto
diferencia_absoluta = abs(numero1 - numero2)

# Imprimir el resultado
print(f'La diferencia en valor absoluto entre {numero1} y {numero2} es: {diferencia_absoluta}')
