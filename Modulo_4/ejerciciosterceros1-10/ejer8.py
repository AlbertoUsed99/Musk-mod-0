from datetime import date, timedelta

def obtener_domingos_de_ano(year):
    domingos = []
    d = date(year, 1, 1)
    d += timedelta(days=(6 - d.weekday()) % 7)  # Primer domingo del año
    while d.year == year:
        domingos.append(d)
        d += timedelta(days=7)
    return domingos

# Para un solo año
ano = 2024
print(f"Domingos del año {ano}:")
for domingo in obtener_domingos_de_ano(ano):
    print(domingo)

# También puedes usarlo para un rango
print("\n--- Domingos del 2000 al 2025 ---")
for anio in range(2000, 2026):
    domingos = obtener_domingos_de_ano(anio)
    print(f"\nAño {anio}:")
    for d in domingos:
        print(d)
