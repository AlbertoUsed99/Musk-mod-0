import pandas as pd

# Diccionarios dados
GermanCars = {
    'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'],
    'Price': [23845, 171995, 135925, 71400]
}

japaneseCars = {
    'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'],
    'Price': [29995, 23600, 61500, 58900]
}

# Convertir a DataFrames
df_german = pd.DataFrame(GermanCars)
df_japanese = pd.DataFrame(japaneseCars)

# Concatenar los DataFrames
df_concatenado = pd.concat([df_german, df_japanese], ignore_index=True)

# Mostrar resultado
print("DataFrame concatenado:")
print(df_concatenado)
