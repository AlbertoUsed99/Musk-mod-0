import pandas as pd
import matplotlib.pyplot as plt
import os

# Ruta al archivo CSV dentro de la carpeta T4
csv_path = os.path.join('T4', 'csvcompany_sales_data.csv')

# Leer el CSV
data = pd.read_csv(csv_path)

# Lista de productos (ajusta según las columnas de tu CSV)
productos = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']

# Sumar las ventas totales anuales para cada producto
ventas_totales = data[productos].sum()

# Crear gráfico circular
plt.figure(figsize=(8,8))
plt.pie(ventas_totales, labels=productos, autopct='%1.1f%%', startangle=140, shadow=True)

plt.title('Porcentaje de unidades vendidas por producto en el último año')
plt.axis('equal')  # Para que el gráfico sea un círculo perfecto
plt.show()
