
# habriendo archivos con with open
with open(r"C:\Users\Usuario\Documents\notas_programacion\Python_Hello\archivos\hola.txt",encoding='UTF-8') as archivo:
    contenido = archivo.read()
    print(contenido)

# no es necesesario cerrar el archivo