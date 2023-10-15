
import pandas as pd

# usando la funcion read_csv para leer los datos
# df = pd.read_csv('txt\\datos.csv',names=["name","lastname","age"]) poder cambiarle el nombre a las columnas
df = pd.read_csv('txt\\datos.csv')


#mostrar los datos de la columna nombre
nombre = df['name']

print(df)

