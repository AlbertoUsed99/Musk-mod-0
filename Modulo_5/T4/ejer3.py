import pandas as pd
import matplotlib.pyplot as plt
import os

# Ruta al archivo CSV dentro de la carpeta T4
csv_path = os.path.join('T4', 'csvcompany_sales_data.csv')

# Leer el CSV
data = pd.read_csv(csv_path)

# Lista de nombres de productos que quieres graficar (ajusta según tu CSV)
productos = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']

# Crear rango de meses
meses = range(1, len(data) + 1)

# Graficar multilínea
for producto in productos:
    plt.plot(meses, data[producto], marker='o', linewidth=2, label=producto)

# Etiquetas y título
plt.xlabel('Número de mes')
plt.ylabel('Número de unidades vendidas')
plt.title('Unidades vendidas por mes para cada producto')

# Leyenda fuera del gráfico a la derecha
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.grid(True)
plt.tight_layout()  # Para que no se corte la leyenda

plt.show()
