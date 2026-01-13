#ak1. Haz un programa que lea una secuencia de caracteres acabada en punto y que escriba cuántas letras ‘a’ contiene.
def main():
    # Solicitar al usuario que ingrese la secuencia de caracteres
    secuencia = input("Introduce una secuencia de caracteres terminada en punto: ")

    # Verificar que la secuencia termine en un punto
    if not secuencia.endswith('.'):
        print("La secuencia debe terminar con un punto.")
        return

    # Contar las letras 'a' (mayúsculas y minúsculas)
    contador_a = secuencia.lower().count('a')

    # Mostrar el resultado
    print(f"La secuencia contiene {contador_a} letras 'a'.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
#2. Haz un programa que encuentre todas las apariciones de una subcadena en una cadena dada.
def encontrar_apariciones(cadena, subcadena):
    """
    Encuentra todas las apariciones de una subcadena en una cadena dada.

    :param cadena: Cadena principal donde buscar.
    :param subcadena: Subcadena que se busca en la cadena principal.
    :return: Lista con las posiciones de inicio de cada aparición de la subcadena.
    """
    posiciones = []
    inicio = 0

    while inicio < len(cadena):
        # Buscar la posición de la subcadena
        posicion = cadena.find(subcadena, inicio)
        if posicion == -1:
            # Si no se encuentra más, salir del bucle
            break
        posiciones.append(posicion)
        # Continuar la búsqueda desde la posición siguiente
        inicio = posicion + len(subcadena)

    return posiciones

# Ejemplo de uso
cadena_principal = input("Ingresa la cadena principal: ")
subcadena_buscar = input("Ingresa la subcadena que deseas buscar: ")

apariciones = encontrar_apariciones(cadena_principal, subcadena_buscar)

if apariciones:
    print(f"La subcadena '{subcadena_buscar}' se encuentra en las posiciones: {apariciones}")
else:
    print(f"La subcadena '{subcadena_buscar}' no se encuentra en la cadena principal.")

#3. Haz un programa que invierta una cadena dada.
def invertir_cadena(cadena):
    """
    Invierte una cadena dada.

    :param cadena: Cadena que se desea invertir.
    :return: Cadena invertida.
    """
    return cadena[::-1]

# Ejemplo de uso
cadena_principal = input("Ingresa la cadena que deseas invertir: ")

cadena_invertida = invertir_cadena(cadena_principal)
print(f"La cadena invertida es: {cadena_invertida}")
#4. Haz un programa que divida una cadena en guiones.
def dividir_en_guiones(cadena):
    """
    Divide una cadena en sus caracteres separados por guiones.

    :param cadena: Cadena que se desea dividir.
    :return: Cadena con los caracteres separados por guiones.
    """
    return "-".join(cadena)

# Ejemplo de uso
cadena_principal = input("Ingresa la cadena que deseas dividir en guiones: ")

cadena_dividida = dividir_en_guiones(cadena_principal)
print(f"La cadena dividida es: {cadena_dividida}")
#5. Haz un programa que añada una nueva cadena en medio de una cadena dada.
def insertar_cadena(cadena, nueva_cadena):
    """
    Inserta una nueva cadena en el medio de una cadena dada.

    :param cadena: Cadena original.
    :param nueva_cadena: Cadena que se desea insertar.
    :return: Cadena resultante con la nueva cadena insertada en el medio.
    """
    mitad = len(cadena) // 2
    return cadena[:mitad] + nueva_cadena + cadena[mitad:]

# Ejemplo de uso
cadena_principal = input("Ingresa la cadena principal: ")
nueva_cadena = input("Ingresa la nueva cadena a insertar: ")

cadena_resultante = insertar_cadena(cadena_principal, nueva_cadena)
print(f"La cadena resultante es: {cadena_resultante}")
#7. Haz un programa que elimine cadenas vacías de una lista de cadenas.
def eliminar_cadenas_vacias(lista_cadenas):
    """
    Elimina las cadenas vacías de una lista de cadenas.

    :param lista_cadenas: Lista de cadenas.
    :return: Nueva lista sin cadenas vacías.
    """
    return [cadena for cadena in lista_cadenas if cadena]

# Ejemplo de uso
lista_cadenas = input("Ingresa una lista de cadenas separadas por comas: ").split(",")

lista_sin_vacias = eliminar_cadenas_vacias(lista_cadenas)
print(f"La lista sin cadenas vacías es: {lista_sin_vacias}")
#8. Haz un programa que elimine símbolos especiales / signos de puntuación de una cadena.
def eliminar_simbolos(cadena):
    """
    Elimina símbolos especiales y signos de puntuación de una cadena.

    :param cadena: Cadena de entrada.
    :return: Cadena sin símbolos especiales ni signos de puntuación.
    """
    signos_puntuacion = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return ''.join(caracter for caracter in cadena if caracter not in signos_puntuacion)

# Ejemplo de uso
cadena_principal = input("Ingresa la cadena de la que deseas eliminar símbolos: ")

cadena_sin_simbolos = eliminar_simbolos(cadena_principal)
print(f"La cadena sin símbolos es: {cadena_sin_simbolos}")
#9. Haz un programa que encuentre palabras con letras y números.
def encontrar_palabras_con_letras_y_numeros(cadena):
    """
    Encuentra palabras que contienen tanto letras como números en una cadena.

    :param cadena: Cadena de entrada.
    :return: Lista de palabras que contienen letras y números.
    """
    palabras = cadena.split()
    resultado = []

    for palabra in palabras:
        tiene_letra = any(caracter.isalpha() for caracter in palabra)
        tiene_numero = any(caracter.isdigit() for caracter in palabra)
        if tiene_letra and tiene_numero:
            resultado.append(palabra)

    return resultado

# Ejemplo de uso
cadena_principal = input("Ingresa una cadena: ")

palabras_mixtas = encontrar_palabras_con_letras_y_numeros(cadena_principal)
print(f"Las palabras con letras y números son: {palabras_mixtas}")
#10. Haz un programa que sustituya cada símbolo especial por # en la siguiente cadena.
def sustituir_simbolos_por_numeral(cadena):
    """
    Sustituye cada símbolo especial en una cadena por el carácter #.

    :param cadena: Cadena de entrada.
    :return: Cadena con los símbolos especiales reemplazados por #.
    """
    signos_puntuacion = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return ''.join('#' if caracter in signos_puntuacion else caracter for caracter in cadena)

# Ejemplo de uso
cadena_principal = input("Ingresa la cadena con símbolos que deseas sustituir: ")

cadena_sustituida = sustituir_simbolos_por_numeral(cadena_principal)
print(f"La cadena con símbolos sustituidos es: {cadena_sustituida}")

#LISTAS

#1. Haz un programa que lea una lista dado su tamaño e imprima el segundo elemento (si existe).
def leer_lista_y_imprimir_segundo():
    """
    Lee una lista dado su tamaño e imprime el segundo elemento si existe.
    """
    tamano = input("Ingresa el tamaño de la lista: ")
    if not tamano.isdigit() or int(tamano) <= 0:
        print("El tamaño de la lista debe ser un número mayor que 0.")
        return

    tamano = int(tamano)
    lista = []
    for i in range(tamano):
        elemento = input(f"Ingresa el elemento {i + 1}: ")
        lista.append(elemento)

    if len(lista) > 1:
        print(f"El segundo elemento de la lista es: {lista[1]}")
    else:
        print("La lista no tiene un segundo elemento.")

# Ejemplo de uso
leer_lista_y_imprimir_segundo()

#2. Haz un programa que lea una secuencia no vacía de enteros acabada en -1, y que escriba cuántos son iguales al último.
def contar_iguales_al_ultimo():
    """
    Lee una secuencia no vacía de enteros terminada en -1 y cuenta cuántos son iguales al último número válido antes del -1.
    """
    print("Ingresa una secuencia de enteros terminada en -1:")
    secuencia = []

    while True:
        numero = input("Ingresa un número: ")
        if not numero.isdigit() and not (numero.startswith("-") and numero[1:].isdigit()):
            print("Por favor, ingresa un número entero válido.")
            continue

        numero = int(numero)
        if numero == -1:
            break
        secuencia.append(numero)

    if not secuencia:
        print("La secuencia no puede estar vacía.")
        return

    ultimo = secuencia[-1]
    iguales = sum(1 for x in secuencia if x == ultimo)
    print(f"En la secuencia, {iguales} número(s) son iguales al último número ({ultimo}).")

# Ejemplo de uso
contar_iguales_al_ultimo()

#3. Haz un programa que lea secuencias de enteros acabada en -1, y que escriba cada una invirtiendo la orden de sus elementos.
# Inicializamos una lista vacía para almacenar los números
numeros = []

# Leemos los números hasta encontrar el -1
while True:
    numero = int(input("Introduce un número (-1 para terminar): "))
    if numero == -1:
        break
    numeros.append(numero)

# Invertimos la lista
numeros_invertidos = numeros[::-1]

# Mostramos la lista invertida
print("Lista invertida:", numeros_invertidos)

#4. Haz un programa que lea n palabras, y que escriba cada una invirtiendo la orden de sus caracteres.
# Leemos el número de palabras
n = int(input("Introduce el número de palabras: "))

# Leemos las palabras y las almacenamos en una lista
palabras = []
for i in range(n):
    palabra = input(f"Introduce la palabra {i+1}: ")
    palabras.append(palabra)

# Invertimos las palabras y las mostramos
for palabra in palabras:
    print(palabra[::-1])

#5. Haz un programa que lea una secuencia de números mientras sean positivos y que escriba la media.
# Inicializamos variables para contar la cantidad de números y acumular su suma
suma = 0
cantidad = 0

# Leemos números hasta que el usuario ingrese un número no positivo
while True:
    numero = int(input("Introduce un número positivo (o un número no positivo para terminar): "))
    
    if numero <= 0:
        break
    
    suma += numero
    cantidad += 1

# Si se han introducido números positivos, calculamos y mostramos la media
if cantidad > 0:
    media = suma / cantidad
    print(f"La media de los números introducidos es: {media}")
else:
    print("No se han introducido números positivos.")

#6. Haz un programa que devuelva la concatenación de v1 y v2, v1 y v2 son dos listas de tamaño n y m. Es decir, hay que devolver un vector que tenga los elementos de v1 seguidos de los elementos de v2.
# Leemos las dos listas
v1 = [int(x) for x in input("Introduce los elementos de la primera lista (separados por espacio): ").split()]
v2 = [int(x) for x in input("Introduce los elementos de la segunda lista (separados por espacio): ").split()]

# Concatenamos las dos listas
v_concatenado = v1 + v2

# Mostramos el resultado
print("La concatenación de v1 y v2 es:", v_concatenado)

#7. Haz un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
l = [50, 75, 46, 22, 80, 65, 8]

print(min(l))
print(max(l))

#8. Haz un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
# Lista de asignaturas del curso
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Mostramos las asignaturas por pantalla
print("Las asignaturas del curso son:")
for asignatura in asignaturas:
    print(asignatura)

#9. Haz un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
# Lista de números del 1 al 10
numeros = list(range(1, 11))

# Mostramos los números en orden inverso separados por comas
print("Números en orden inverso:", ", ".join(map(str, numeros[::-1])))

#10. Haz un programa que concatene dos listas del mismo tamaño n alternando elementos de una lista y otra.
# Leemos las dos listas
v1 = [int(x) for x in input("Introduce los elementos de la primera lista (separados por espacio): ").split()]
v2 = [int(x) for x in input("Introduce los elementos de la segunda lista (separados por espacio): ").split()]

# Verificamos que las listas tengan el mismo tamaño
if len(v1) != len(v2):
    print("Error: Las listas deben tener el mismo tamaño.")
else:
    # Creamos una lista alternando elementos de v1 y v2
    v_concatenado = [elem for pair in zip(v1, v2) for elem in pair]
    
    # Mostramos el resultado
    print("La concatenación alternada de las listas es:", v_concatenado)

#11. Haz un programa que itere ambas listas de tamaños n y m (siendo n y m números distintos )simultáneamente e imprima sus elementos.
# Leemos las dos listas
v1 = [int(x) for x in input("Introduce los elementos de la primera lista (separados por espacio): ").split()]
v2 = [int(x) for x in input("Introduce los elementos de la segunda lista (separados por espacio): ").split()]

# Iteramos sobre ambas listas simultáneamente
print("Iterando sobre ambas listas:")
for elem1, elem2 in zip(v1, v2):
    print(f"Lista 1: {elem1}, Lista 2: {elem2}")

# Si las listas son de tamaños diferentes, procesamos los elementos restantes
if len(v1) > len(v2):
    print("Elementos restantes en la lista 1:", v1[len(v2):])
elif len(v2) > len(v1):
    print("Elementos restantes en la lista 2:", v2[len(v1):])

#12. Haz un programa que añada un nuevo elemento 60 a la lista [10, 50, 40, 20, 30] después de un elemento especificado por el usuario. Si el elemento introducido no está presente en la lista debe mostrar el mensaje: 'Elemento no presente en la lista'.
# Lista inicial
lista = [10, 50, 40, 20, 30]

# Mostrar la lista actual
print("Lista actual:", lista)

# Solicitar al usuario un elemento
elemento = int(input("Introduce el elemento después del cual deseas añadir 60: "))

# Verificar si el elemento está en la lista
if elemento in lista:
    # Encontrar la posición del elemento
    indice = lista.index(elemento)
    # Insertar el nuevo elemento después de la posición encontrada
    lista.insert(indice + 1, 60)
    print("Lista actualizada:", lista)
else:
    print("Elemento no presente en la lista.")

#13. Haz un programa que elimine todas las apariciones de un elemento específico introducido por el usuario de la lista [10, 50, 40, 20, 60, 30].
# Lista inicial
lista = [10, 50, 40, 20, 60, 30]

# Mostrar la lista actual
print("Lista actual:", lista)

# Solicitar al usuario el elemento a eliminar
elemento = int(input("Introduce el elemento que deseas eliminar: "))

# Verificar si el elemento está en la lista
if elemento in lista:
    # Eliminar todas las apariciones del elemento
    lista = [x for x in lista if x != elemento]
    print("Lista actualizada:", lista)
else:
    print("El elemento no está presente en la lista.")




#Tuplas


#1. Haz una programa que invierta una tupla.
# Tupla inicial
tupla = (10, 20, 30, 40, 50)

# Invertimos la tupla
tupla_invertida = tupla[::-1]

# Mostramos la tupla invertida
print("Tupla original:", tupla)
print("Tupla invertida:", tupla_invertida)

#2. Haz un programa que acceda al valor 15 de la tupla.
# Tupla de ejemplo
tupla = (5, 10, 15, 20, 25)

# Buscamos el valor 15
if 15 in tupla:
    indice = tupla.index(15)
    print(f"El valor 15 está en la posición {indice} de la tupla.")
else:
    print("El valor 15 no está en la tupla.")

#3. Haz un programa que declare una tupla con un solo elemento 10.
# Declaramos una tupla con un solo elemento
tupla = (10,)

# Mostramos la tupla
print("La tupla con un solo elemento es:", tupla)

#4. Haz un programa que inicialice el diccionario con valores por defecto.
# Inicializamos un diccionario con valores por defecto
diccionario = {
    "clave1": "valor por defecto 1",
    "clave2": "valor por defecto 2",
    "clave3": "valor por defecto 3"
}

# Mostramos el diccionario inicializado
print("Diccionario inicializado con valores por defecto:")
print(diccionario)


#5. Haz un programa que cree un diccionario extrayendo las claves de un diccionario dado.
# Diccionario original
diccionario_original = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

# Claves que queremos extraer
claves_a_extraer = ["nombre", "ciudad"]

# Crear un nuevo diccionario con las claves extraídas
diccionario_extraido = {clave: diccionario_original[clave] for clave in claves_a_extraer if clave in diccionario_original}

# Mostramos el nuevo diccionario
print("Nuevo diccionario con claves extraídas:")
print(diccionario_extraido)

#6. Haz un programa que elimine una lista de claves de un diccionario.

# Diccionario original
diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

# Lista de claves a eliminar
claves_a_eliminar = ["edad", "profesion"]

# Eliminamos las claves del diccionario
for clave in claves_a_eliminar:
    diccionario.pop(clave, None)  # pop con None evita errores si la clave no existe

# Mostramos el diccionario actualizado
print("Diccionario después de eliminar las claves:")
print(diccionario)

#7. Haz un programa que compruebe si un valor existe en un diccionario.

# Diccionario de ejemplo
sample_dict = {'a': 100, 'b': 200, 'c': 300}

# Valor a buscar
x = 200

# Verificar si el valor existe en el diccionario
if x in sample_dict.values():
    print(f'{x} está presente en el diccionario.')
else:
    print(f'{x} no se encuentra en el diccionario.')

#8. Haz un programa que cambie el nombre de la clave de un diccionario.

def cambiar_nombre_clave(diccionario, clave_actual, nueva_clave):
    """
    Cambia el nombre de una clave en un diccionario.

    :param diccionario: Diccionario donde se cambiará la clave.
    :param clave_actual: Clave que se desea cambiar.
    :param nueva_clave: Nuevo nombre para la clave.
    :return: Diccionario con la clave renombrada.
    """
    if clave_actual in diccionario:
        diccionario[nueva_clave] = diccionario.pop(clave_actual)
    else:
        print("La clave especificada no existe en el diccionario.")
    return diccionario

# Ejemplo de uso
diccionario = {"nombre": "Carlos", "edad": 25, "ciudad": "Madrid"}
clave_actual = input("Ingresa la clave actual que deseas cambiar: ")
nueva_clave = input("Ingresa el nuevo nombre de la clave: ")

diccionario_actualizado = cambiar_nombre_clave(diccionario, clave_actual, nueva_clave)
print(f"Diccionario actualizado: {diccionario_actualizado}")

#9. Haz un programa que obtenga la clave de un valor mínimo del siguiente diccionario.

def obtener_clave_valor_minimo(diccionario):
    """
    Obtiene la clave del valor mínimo en un diccionario.

    :param diccionario: Diccionario con valores numéricos.
    :return: Clave asociada al valor mínimo.
    """
    if not diccionario:
        return "El diccionario está vacío."
    
    clave_minima = min(diccionario, key=diccionario.get)
    return clave_minima

# Ejemplo de uso
diccionario = {"a": 10, "b": 5, "c": 8, "d": 2}
clave_min = obtener_clave_valor_minimo(diccionario)
print(f"La clave con el valor mínimo es: {clave_min}")


#10. Haz un programa que cambie el valor de una clave en un diccionario anidado.

def cambiar_valor_clave_anidada(diccionario, clave_externa, clave_interna, nuevo_valor):
    """
    Cambia el valor de una clave en un diccionario anidado.

    :param diccionario: Diccionario principal con otro diccionario dentro.
    :param clave_externa: Clave que contiene el diccionario anidado.
    :param clave_interna: Clave dentro del diccionario anidado cuyo valor se cambiará.
    :param nuevo_valor: Nuevo valor para la clave interna.
    :return: Diccionario actualizado.
    """
    if clave_externa in diccionario and isinstance(diccionario[clave_externa], dict):
        if clave_interna in diccionario[clave_externa]:
            diccionario[clave_externa][clave_interna] = nuevo_valor
        else:
            print("La clave interna no existe en el diccionario anidado.")
    else:
        print("La clave externa no existe o no contiene un diccionario anidado.")
    return diccionario

# Ejemplo de uso
diccionario = {
    "usuario1": {"nombre": "Carlos", "edad": 25},
    "usuario2": {"nombre": "Ana", "edad": 30}
}

clave_externa = input("Ingresa la clave externa: ")
clave_interna = input("Ingresa la clave interna: ")
nuevo_valor = input("Ingresa el nuevo valor: ")

diccionario_actualizado = cambiar_valor_clave_anidada(diccionario, clave_externa, clave_interna, nuevo_valor)
print(f"Diccionario actualizado: {diccionario_actualizado}")


#Sets

#1. Haz un programa que añada una lista de elementos a un conjunto.
def agregar_lista_a_conjunto(conjunto, lista):
    """
    Añade los elementos de una lista a un conjunto.

    :param conjunto: Conjunto original.
    :param lista: Lista de elementos a añadir.
    :return: Conjunto actualizado con los nuevos elementos.
    """
    conjunto.update(lista)
    return conjunto

# Ejemplo de uso
conjunto = {1, 2, 3}
lista = [3, 4, 5, 6]

conjunto_actualizado = agregar_lista_a_conjunto(conjunto, lista)
print(f"El conjunto actualizado es: {conjunto_actualizado}")
#2. Haz un programa que devuelva un nuevo conjunto de elementos idénticos de dos conjuntos.
def elementos_identicos(conjunto1, conjunto2):
    """
    Devuelve un nuevo conjunto con los elementos comunes entre dos conjuntos.

    :param conjunto1: Primer conjunto.
    :param conjunto2: Segundo conjunto.
    :return: Conjunto con elementos idénticos en ambos conjuntos.
    """
    return conjunto1 & conjunto2  # Operador de intersección

# Ejemplo de uso
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}

resultado = elementos_identicos(conjunto1, conjunto2)
print(f"Elementos idénticos en ambos conjuntos: {resultado}")

#3. Haz un programa que obtenga sólo elementos únicos de dos conjuntos.
def elementos_unicos(conjunto1, conjunto2):
    """
    Devuelve un nuevo conjunto con los elementos únicos de dos conjuntos.

    :param conjunto1: Primer conjunto.
    :param conjunto2: Segundo conjunto.
    :return: Conjunto con elementos únicos en ambos conjuntos.
    """
    return conjunto1 ^ conjunto2  # Operador de diferencia simétrica

# Ejemplo de uso
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}

resultado = elementos_unicos(conjunto1, conjunto2)
print(f"Elementos únicos en ambos conjuntos: {resultado}")

#4. Haz un programa que actualice el primer conjunto con elementos que no existen en el segundo conjunto.
def actualizar_conjunto(conjunto1, conjunto2):
    """
    Actualiza el primer conjunto con elementos que no existen en el segundo conjunto.

    :param conjunto1: Primer conjunto a actualizar.
    :param conjunto2: Segundo conjunto con elementos a excluir.
    """
    conjunto1 -= conjunto2  # Operador de diferencia para eliminar elementos de conjunto2

# Ejemplo de uso
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}

actualizar_conjunto(conjunto1, conjunto2)
print(f"Primer conjunto actualizado: {conjunto1}")
#5. Haz un programa que elimine elementos del conjunto a la vez.
def eliminar_elementos(conjunto, elementos):
    conjunto -= elementos

conjunto1 = {1, 2, 3, 4, 5}
eliminar_elementos(conjunto1, {1, 2})
print(f"Conjunto después de eliminar elementos: {conjunto1}")
#6. Haz un programa que devuelva un conjunto de elementos presentes en el conjunto A o B, pero no en ambos.
def diferencia_simetrica(conjunto1, conjunto2):
    return conjunto1 ^ conjunto2

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}
resultado = diferencia_simetrica(conjunto1, conjunto2)
print(f"Elementos en A o B, pero no en ambos: {resultado}")
#7. Haz un programa que compruebe si dos conjuntos tienen algún elemento en común. En caso afirmativo, mostrar los elementos comunes.
def elementos_comunes(conjunto1, conjunto2):
    comunes = conjunto1 & conjunto2
    if comunes:
        print(f"Elementos comunes: {comunes}")
    else:
        print("No hay elementos en común.")

elementos_comunes(conjunto1, conjunto2)

#8. Haz un programa que actualice el conjunto1 añadiendo elementos del conjunto2, excepto los elementos comunes.
def actualizar_sin_comunes(conjunto1, conjunto2):
    conjunto1 ^= conjunto2

actualizar_sin_comunes(conjunto1, conjunto2)
print(f"Conjunto actualizado sin elementos comunes: {conjunto1}")
#9. Haz un programa que actualice el conjunto1 añadiendo elementos del conjunto2, excepto los elementos comunes.
def actualizar_conjunto1(conjunto1, conjunto2):
    conjunto1 |= conjunto2 - conjunto1

actualizar_conjunto1(conjunto1, conjunto2)
print(f"Conjunto actualizado con elementos de conjunto2, excepto los comunes: {conjunto1}")