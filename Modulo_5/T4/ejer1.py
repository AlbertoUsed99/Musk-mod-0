import pandas as pd
import matplotlib.pyplot as plt
import os

# Mostrar carpeta actual para verificar
print("Carpeta actual de trabajo:", os.getcwd())

# Ruta al archivo CSV dentro de la carpeta T4
csv_path = os.path.join('T4', 'csvcompany_sales_data.csv')

# Leer el CSV
data = pd.read_csv(csv_path)

# Crear rango de meses (asumiendo que cada fila es un mes)
meses = range(1, len(data) + 1)

# Cambia 'total_profit' por el nombre correcto de la columna de beneficio total si es diferente
beneficio_total = data['total_profit']

# Graficar
plt.plot(meses, beneficio_total, marker='o', linestyle='-')
plt.xlabel('Número de mes')
plt.ylabel('Beneficio total')
plt.title('Beneficio total mensual')
plt.grid(True)
plt.show()
