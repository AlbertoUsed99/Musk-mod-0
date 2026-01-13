def dividir(a, b):
    try:
        resultado = a / b
        print("Resultado:", resultado)
    except TypeError:
        print("Los parámetros deben ser número enteros")
    except ZeroDivisionError:
        print("El divisor no puede ser 0")
    finally:
        print("Ejecución completada.")

# Ejemplos de uso:
dividir(10, 2)     # Correcto
dividir(10, 0)     # ZeroDivisionError
dividir(10, "a")   # TypeError
