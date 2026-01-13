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

# Crear gráfico de barras apiladas
plt.figure(figsize=(10, 6))

bottom = np.zeros(len(data))  # para acumular las alturas

for producto in productos:
    plt.bar(meses, data[producto], bottom=bottom, label=producto)
    bottom += data[producto]

# Etiquetas y título
plt.xlabel('Número de mes')
plt.ylabel('Unidades vendidas')
plt.title('Ventas mensuales de productos (Diagrama de pila)')

# Leyenda fuera del gráfico
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()
