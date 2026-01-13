import pandas as pd
import matplotlib.pyplot as plt
import os

# Ruta al archivo CSV dentro de la carpeta T4
csv_path = os.path.join('T4', 'csvcompany_sales_data.csv')

# Leer el CSV
data = pd.read_csv(csv_path)

# Crear rango de meses (asumiendo que cada fila es un mes)
meses = range(1, len(data) + 1)

# Extraer datos de ventas de pasta de dientes (ajusta el nombre si es diferente)
ventas_pasta = data['toothpaste']

# Crear gráfico de dispersión
plt.scatter(meses, ventas_pasta, color='blue', label='Ventas Pasta de Dientes')

# Etiquetas y título
plt.xlabel('Número de mes')
plt.ylabel('Unidades vendidas')
plt.title('Ventas mensuales de pasta de dientes')

# Cuadrícula con estilo "-"
plt.grid(True, linestyle='-')

plt.legend()
plt.show()
