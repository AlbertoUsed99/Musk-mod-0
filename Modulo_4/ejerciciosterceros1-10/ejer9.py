from datetime import date

def contar_lunes_primer_dia(inicio, fin):
    contador = 0
    for anio in range(inicio, fin + 1):
        for mes in range(1, 13):
            if date(anio, mes, 1).weekday() == 0:  # 0 = lunes
                contador += 1
                print(f"{anio}-{mes:02d}-01 es lunes")
    return contador

inicio = 2015
fin = 2016
total_lunes = contar_lunes_primer_dia(inicio, fin)
print(f"\nTotal de lunes que cayeron en el primer día del mes entre {inicio} y {fin}: {total_lunes}")
