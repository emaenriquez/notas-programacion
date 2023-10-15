
diccionario = {
    'nombre': 'emanuel',
    'apellido': 'enriquez',
    'años': 20
}

# devuelve las claves (tambien nos sirve para iterar)
claves = diccionario.keys()

# devuelve el valor de la claves
claves = diccionario.get("nombre")

# elimina todos los valores
diccionario.clear()

# eliminando un elemento del diccionario
diccionario.pop('nombre')

# obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)