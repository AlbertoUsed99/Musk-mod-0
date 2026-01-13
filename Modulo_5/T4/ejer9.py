import pandas as pd
import matplotlib.pyplot as plt
import os

# Ruta al archivo CSV dentro de la carpeta T4
csv_path = os.path.join('T4', 'csvcompany_sales_data.csv')

# Leer el CSV
data = pd.read_csv(csv_path)

# Crear rango de meses
meses = range(1, len(data) + 1)

# Datos de ventas de jabón de baño
ventas_jabon = data['bathingsoap']

# Crear figura y un subplot
fig, ax = plt.subplots(figsize=(8, 5))

# Graficar ventas de jabón de baño
ax.plot(meses, ventas_jabon, marker='o', linestyle='-', color='green')

# Etiquetas y título
ax.set_xlabel('Número de mes')
ax.set_ylabel('Unidades vendidas')
ax.set_title('Ventas mensuales de jabón de baño')

ax.grid(True)

plt.show()
