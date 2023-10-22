
import pandas as pd

# usando la funcion read_csv para leer los datos
# df = pd.read_csv('txt\\datos.csv',names=["name","lastname","age"]) poder cambiarle el nombre a las columnas

file_path = 'archivos\\datos.csv'
df = pd.read_csv(file_path, encoding='utf-8')


#mostrar los datos de la columna nombre
nombre = df['name']

cadena = '0123456789'
# print(cadena[:2])

# ordenando el dataframe por la edad 

df_ordenado = df.sort_values("edad")

print(df_ordenado)