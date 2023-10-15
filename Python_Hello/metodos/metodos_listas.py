#crea una listas
listas = list([10,21,21,21,21,21,42,21,4243,31])

#devuele la cantidad de elmentos de una lista
cantidad_elementos_lista = len(listas)

# agregar elementos a una lista
listas.append(12)

# agregar elementos a una lista en un indice especifico
listas.insert(0,27)

# agregando varios elementos a la lista
listas.extend([True,1021,90])

#eliminando un elemento de un lista(por su indice)
listas.pop(0)

#remueve un elemento de la lista por su valor
listas.remove("batman")

#elimina todos los elementos de la lista
listas.clear()

#ordena los elementos de forma ascendente si usamos reverse=true da vuelta la lista
listas.sort(reverse=True)
#invirtiendo los elementos de una lista
listas.reverse()
print(listas)
