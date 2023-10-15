
diccionario = {
    'Nombre':'Emanuel',
    'Apellido': 'Enriquez',
    'altura': 1.75
}
# recorriendo diccionario con items para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    valor = datos[1]
    print(f"la key es: {key} y el valor es: {valor}")


# recorriendo diccionario con items para obtener la clave
for key in diccionario.items():
    print(key)