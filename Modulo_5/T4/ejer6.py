import pandas as pd
import matplotlib.pyplot as plt
import os

# Ruta al archivo CSV dentro de la carpeta T4
csv_path = os.path.join('T4', 'csvcompany_sales_data.csv')

# Leer el CSV
data = pd.read_csv(csv_path)

# Crear rango de meses
meses = range(1, len(data) + 1)

# Datos de ventas de jabón de baño (ajusta el nombre de la columna si es necesario)
ventas_jabon = data['bathingsoap']

# Crear gráfico de barras
plt.bar(meses, ventas_jabon, color='purple')

# Etiquetas y título
plt.xlabel('Número de mes')
plt.ylabel('Unidades vendidas')
plt.title('Ventas mensuales de jabón de baño')

plt.grid(axis='y', linestyle='--', alpha=0.7)

# Guardar el gráfico en disco (puedes cambiar la ruta y el nombre)
plt.savefig('grafico_ventas_jabon.png')

plt.show()
