import pandas as pd
import matplotlib.pyplot as plt
import os

# Ruta al archivo CSV dentro de la carpeta T4
csv_path = os.path.join('T4', 'csvcompany_sales_data.csv')

# Leer el CSV
data = pd.read_csv(csv_path)

# Extraer la columna de beneficio total (ajusta el nombre si es diferente)
beneficio_total = data['total_profit']

# Crear histograma
plt.hist(beneficio_total, bins=10, color='green', edgecolor='black')

# Etiquetas y título
plt.xlabel('Beneficio total')
plt.ylabel('Frecuencia')
plt.title('Histograma de beneficio total mensual')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
