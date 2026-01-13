import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Ruta al archivo CSV dentro de la carpeta T4
csv_path = os.path.join('T4', 'csvcompany_sales_data.csv')

# Leer el CSV
data = pd.read_csv(csv_path)

# Crear rango de meses
meses = np.arange(1, len(data) + 1)

# Datos de ventas (ajusta los nombres de columnas si es necesario)
ventas_crema = data['facecream']
ventas_lavado = data['facewash']

# Ancho de las barras
ancho = 0.35

# Posiciones para las barras
pos_crema = meses - ancho/2
pos_lavado = meses + ancho/2

# Crear el gráfico de barras
plt.bar(pos_crema, ventas_crema, width=ancho, label='Crema Facial', color='skyblue')
plt.bar(pos_lavado, ventas_lavado, width=ancho, label='Lavado de Cara', color='salmon')

# Etiquetas y título
plt.xlabel('Número de mes')
plt.ylabel('Unidades vendidas')
plt.title('Ventas mensuales: Crema Facial vs Lavado de Cara')

# Ajustar ticks del eje x para que estén centrados en las barras
plt.xticks(meses)

plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
