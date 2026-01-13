from datetime import datetime, timedelta

# --- CONFIGURACIÓN ---
HORARIO_INICIO = 9   # 09:00
HORARIO_FIN = 18     # 18:00

def es_dia_habil(fecha):
    """Verifica si la fecha cae en un día hábil (lunes a viernes)."""
    return fecha.weekday() < 5  # 0 = lunes, 6 = domingo

def siguiente_dia_habil(fecha):
    """Devuelve el siguiente día hábil a las 09:00."""
    fecha += timedelta(days=1)
    while not es_dia_habil(fecha):
        fecha += timedelta(days=1)
    return fecha.replace(hour=HORARIO_INICIO, minute=0, second=0, microsecond=0)

def calcular_fecha_entrega(fecha_inicio, dias_habiles):
    fecha_actual = fecha_inicio

    # Paso 1: Avanzar días hábiles
    while dias_habiles > 0:
        fecha_actual += timedelta(days=1)
        if es_dia_habil(fecha_actual):
            dias_habiles -= 1

    # Paso 2: Ajustar horario laboral
    if fecha_actual.hour < HORARIO_INICIO:
        fecha_actual = fecha_actual.replace(hour=HORARIO_INICIO, minute=0, second=0, microsecond=0)
    elif fecha_actual.hour >= HORARIO_FIN:
        fecha_actual = siguiente_dia_habil(fecha_actual)

    return fecha_actual

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    # Pedir datos al usuario
    fecha_str = input("Ingrese la fecha de inicio (formato: YYYY-MM-DD HH:MM): ")
    dias_habiles = int(input("Ingrese la cantidad de días hábiles a sumar: "))

    # Convertir a objeto datetime
    fecha_inicio = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
    fecha_entrega = calcular_fecha_entrega(fecha_inicio, dias_habiles)

    # Calcular diferencia en horas y minutos
    diferencia = fecha_entrega - fecha_inicio
    horas, resto = divmod(diferencia.total_seconds(), 3600)
    minutos = resto // 60

    # Mostrar resultados
    print("\n--- RESULTADOS ---")
    print(f"📦 Fecha de inicio: {fecha_inicio}")
    print(f"📦 Fecha estimada de entrega: {fecha_entrega}")
    print(f"⏳ Diferencia total: {int(horas)} horas y {int(minutos)} minutos")
