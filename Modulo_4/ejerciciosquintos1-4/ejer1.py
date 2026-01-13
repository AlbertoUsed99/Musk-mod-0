def generar_excepcion():
    try:
        # Esto causará una excepción (división por cero)
        resultado = 10 / 0
    except Exception as e:
        print("Tipo de excepción:", type(e).__name__)
        print("Argumentos de la excepción:", e.args)
        print("Mensaje de error:", str(e))

# Ejemplo de uso
generar_excepcion()
