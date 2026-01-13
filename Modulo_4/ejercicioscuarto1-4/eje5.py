def generar_senares(n):
    contador = 0
    numero = 1
    while contador < n:
        yield numero
        numero += 2
        contador += 1

# Ejemplo de uso
for num in generar_senares(5):
    print(num)
