def dividir(a, b):
    try:
        resultado = a / b
        print("Resultado:", resultado)
    except TypeError:
        print("Los parámetros deben ser número enteros")
    except ZeroDivisionError:
        print("El divisor no puede ser 0")

# Ejemplos de uso:
dividir(10, 2)     # Correcto → Resultado: 5.0
dividir(10, 0)     # ZeroDivisionError → El divisor no puede ser 0
dividir(10, "a")   # TypeError → Los parámetros deben ser número enteros
