
#creando diccionario con dict
# no podemos crear listas,tuplas diccionario sino usamos su respectiva funcion
diccionario = dict(nombre="Emanuel",apellido="Enriquez")

# las listas no pueden ser claves y usamos fronset para meter conjunto
diccionario = {frozenset(["dato1","dato2"]):"jajaja"}

#creamos diccionario con fromkeys() valor por defecto:none
diccionario = dict.fromkeys(["nombre","apellido"])

#creamos diccionario con fromkeys() cambiamos el valor por defecto a "nose"
diccionario = dict.fromkeys(["nombre","apellido"],"nose")

print(diccionario)