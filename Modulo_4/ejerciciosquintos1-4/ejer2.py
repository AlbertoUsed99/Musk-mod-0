# Definición de la excepción personalizada
class NegativeDifferenceException(Exception):
    def __init__(self, diferencia):
        super().__init__(f"Diferencia negativa detectada: {diferencia}")
        self.diferencia = diferencia

# Función que calcula la diferencia y lanza la excepción si es negativa
def calcular_diferencia(a, b):
    diferencia = a - b
    if diferencia < 0:
        raise NegativeDifferenceException(diferencia)
    return diferencia

# Ejemplo de uso
try:
    resultado = calcular_diferencia(3, 7)
    print("Diferencia:", resultado)
except NegativeDifferenceException as e:
    print("Se lanzó una excepción personalizada:")
    print("Tipo:", type(e).__name__)
    print("Mensaje:", str(e))
