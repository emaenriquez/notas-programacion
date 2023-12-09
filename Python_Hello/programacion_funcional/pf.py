
from functools import reduce
from operator import add

# Programación Funcional en Python

# Se basa principalmente en el uso de funciones, siendo las mismas practicamente la única herramienta que el lenguaje nos ofrece.

# map en Python
# La función map toma dos entradas:
    # Una lista o iterable que será modificado en una nueva.
    # Una función, que será aplicada a cada uno de los elementos de la lista o iterable anterior.

# map(funcion_a_aplicar, entrada_iterable)

lista = [1,2,3,4,5]

def por_dos(x):
    return x * 2

lista_pordos = map(por_dos,lista)
lista_pordos = map(lambda x: 2 * x, lista)

print(list(lista_pordos))

# filter en Python
# La función filter también recibe una función y una lista pero el resultado es la lista inicial filtrada. Es decir, se pasa cada elemento de la lista por la función, y sólo si su resultado es True, se incluye en la nueva lista.

lista = [7,4,16,3,8]

def es_par(x):
    return x % 2 == 0

pares = filter(es_par,lista)

print(list(pares))

# reduce en Python
# Por último, podemos usar reduce para reducir todos los elementos de la entrada a un único valor aplicando un determinado criterio

lista = [1,2,3,4,5]

suma = reduce(lambda acc, val: acc + val,lista)
suma = reduce(add,lista)
multiplicacion = reduce(lambda acc, val: acc * val,lista)
print(suma)


personas = [
    {'Nombre': 'Alicia', 'Edad': 22},
    {'Nombre': 'Bob', 'Edad': 29},
    {'Nombre': 'Charlie', 'Edad': 33}
]

suma_edad = reduce(lambda total,p: total + p['Edad'],personas,0)

print(suma_edad/len(personas))

# Características de la Programación Funcional
# prácticamente todo se hace con funciones, y no con bucles.
# La programación funcional prefiere también las funciones puras, es decir, funciones sin side effects. Las funciones puras no dependen de variables externas o globales.

personas = [
    {'Nombre': 'Alicia', 'Edad': 22, 'Sexo': 'F'},
    {'Nombre': 'Bob', 'Edad': 25, 'Sexo': 'M'},
    {'Nombre': 'Charlie', 'Edad': 33, 'Sexo': 'M'},
    {'Nombre': 'Diana', 'Edad': 15, 'Sexo': 'F'},
    {'Nombre': 'Esteban', 'Edad': 30, 'Sexo': 'M'},
    {'Nombre': 'Federico', 'Edad': 44, 'Sexo': 'M'},
]

hombres = list(filter(lambda x: x['Sexo'] == 'M', personas))
suma_edades = reduce(lambda suma, p: suma + p['Edad'], hombres, 0)
media_edad = suma_edades/(len(hombres))
print(hombres)
print(media_edad)