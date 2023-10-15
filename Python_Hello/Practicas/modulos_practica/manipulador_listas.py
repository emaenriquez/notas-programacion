
# Ejercicio 3: Crear un módulo para operaciones con listas
# Crea un módulo llamado "manipulador_listas.py" que contenga las siguientes funciones para operar con listas:


# a) buscar_elemento(lista, elemento): Recibe una lista y un elemento, y devuelve el índice de la primera ocurrencia del elemento en la lista (o -1 si no está presente).
def buscar_elemento(lista,elemento):
    index = []

    for l in lista:
        if(l == elemento):
            index = lista.index(elemento)
            break;
        else:
            return 'el elemento no esta en la lista'
    return f'el indice del elemento que buscamos esta: {index}'

# b) eliminar_elemento(lista, elemento): Recibe una lista y un elemento, y elimina la primera ocurrencia del elemento en la lista (si está presente).
def eleminar_elemento(lista,elemento):
    for l in lista:
        if(l == elemento):
            lista.remove(elemento)
            break
    return f'la lista nueva con el elemento el eliminado es: {lista}'

# c) promedio(lista): Recibe una lista de números y devuelve el promedio de todos los elementos.
def promedio(lista):
    total_elemento = len(lista)
    suma_elemento = sum(lista)
    promedio = suma_elemento / total_elemento
    return f'el promedio de elementos es: {promedio}'

# d) ordenar_lista(lista): Recibe una lista de números y devuelve una nueva lista ordenada de menor a mayor sin modificar la lista original.
def ordenar_lista(list):

    lista_ordenada = sorted(list)
        
    return lista_ordenada