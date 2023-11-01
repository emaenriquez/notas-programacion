
import pandas as pd

# usando la funcion read_csv para leer los datos
# df = pd.read_csv('txt\\datos.csv',names=["name","lastname","age"]) poder cambiarle el nombre a las columnas

file_path =  r"C:\Users\Usuario\Documents\notas_programacion\Python_Hello\archivos\datos.csv"
df = pd.read_csv(file_path)
df2 = pd.read_csv(file_path)


#mostrar los datos de la columna nombre
nombre = df['nombre']

cadena = '0123456789'
# print(cadena[:2])

# ordenando el dataframe por la edad 
df_ordenado_ascendente = df.sort_values("edad")

# ordenandolo de forma desendente
df_ordenado_descendente = df.sort_values('edad',ascending=False)

# concatenando 2 dataFrames
df_concatenado = pd.concat([df,df2])
 
# accediendo a la primera fila con head() desde arriba para abajo
primera_file = df.head(1) 

# accediendo a la utima filas desde abajo hacia arriba
ultimas_fila = df.tail(3)

# accediendo a la cantidad de filas y columnas con shape
# filas_y_columas_totales = df.shape()
# filas_totales = filas_y_columas_totales[0]
# columnas_totales = filas_y_columas_totales[1]
filas_totales,columnas_totales = df.shape


# obteniedno la estadistica del dataframe
df_info = df.describe

# accediendo a un elemento espeficico del data df con loc
elemento_especifico_loc = df.loc[2,'edad']

elemento_especifico_loc = df.loc[:,'apellido']

# accediendo a un elemento espeficico del data df con iloc
elemento_especifico_iloc = df.iloc[2,2]

# accediendo a todas las filas con iloc
apellidos = df.iloc[:,1]

# accediendo a todas las columnas con loc
fila_3 = df.loc[2,:]

# accediendo a todas las columnas con iloc
fila_3 = df.iloc[2,:]

# accediendo a filas con edad > 30

edad_mayor = df.loc[df['edad'] > 30 ,:]

print(df_concatenado)