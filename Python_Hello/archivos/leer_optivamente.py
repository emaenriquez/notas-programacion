
# habriendo archivos con with open
with open('archivos\\hola.txt',encoding='UTF-8') as archivo:
    contenido = archivo.read()
    print(contenido)

# no es necesesario cerrar el archivo