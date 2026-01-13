import pandas as pd
import matplotlib.pyplot as plt
import os

# Ruta al archivo CSV dentro de la carpeta T4
csv_path = os.path.join('T4', 'csvcompany_sales_data.csv')

# Leer el CSV
data = pd.read_csv(csv_path)

# Crear rango de meses (asumiendo que cada fila es un mes)
meses = range(1, len(data) + 1)

# Cambia 'total_profit' por el nombre correcto de la columna de beneficio total o unidades vendidas
beneficio_total = data['total_profit']  # Si la columna se llama diferente, cámbiala aquí

# Graficar con las propiedades de estilo pedidas
plt.plot(meses, beneficio_total, linestyle='--', color='red', marker='o', linewidth=3, label='Beneficio total')

# Etiquetas y título
plt.xlabel('Número de mes')
plt.ylabel('Número de unidades vendidas')
plt.title('Beneficio total mensual')

# Leyenda en la parte inferior derecha
plt.legend(loc='lower right')

plt.grid(True)
plt.show()
