def dobles_inferiores(n):
    for i in range(n):
        yield i * 2

# Ejemplo de uso
for num in dobles_inferiores(5):
    print(num)
