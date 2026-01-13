import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Ruta al archivo CSV dentro de la carpeta T4
csv_path = os.path.join('T4', 'csvcompany_sales_data.csv')

# Leer el CSV
data = pd.read_csv(csv_path)

# Lista de productos (ajusta según tu CSV)
productos = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']

# Crear rango de meses
meses = np.arange(1, len(data) + 1)

# Datos de productos para apilar
ventas_productos = data[productos]

# Crear gráfico de barras apiladas
plt.figure(figsize=(10,6))
plt.bar(meses, ventas_productos[productos[0]], label=productos[0])

bottom = ventas_productos[productos[0]].copy()

for producto in productos[1:]:
    plt.bar(meses, ventas_productos[producto], bottom=bottom, label=producto)
    bottom += ventas_productos[producto]

# Etiquetas y título
plt.xlabel('Número de mes')
plt.ylabel('Unidades vendidas')
plt.title('Ventas mensuales de productos (Diagrama de pila)')

plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
