def prod(l1, l2):
    it1 = iter(l1)
    it2 = iter(l2)
    solution = []

    try:
        while True:
            a = next(it1)
            b = next(it2)
            solution.append(a * b)
    except StopIteration:
        pass

    return solution

# Ejemplo de uso
lista1 = [2, 4, 6]
lista2 = [3, 5, 7]

resultado = prod(lista1, lista2)
print("Resultado de la multiplicación elemento a elemento:", resultado)
