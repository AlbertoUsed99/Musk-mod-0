import pandas as pd

# Diccionarios proporcionados
Car_Price = {
    'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
    'Price': [23845, 17995, 135925, 71400]
}

car_Horsepower = {
    'Company': ['Toyota', 'Honda', 'BMV', 'Audi'],
    'horsepower': [141, 80, 182, 160]
}

# Crear DataFrames a partir de los diccionarios
df_price = pd.DataFrame(Car_Price)
df_power = pd.DataFrame(car_Horsepower)

# Fusionar usando la columna "Company"
df_merged = pd.merge(df_price, df_power, on='Company')

# Mostrar el resultado
print("DataFrame combinado:")
print(df_merged)
