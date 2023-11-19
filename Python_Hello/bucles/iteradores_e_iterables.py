
# mal uso
lista = [5, 4, 9, 2]
i = 0
while i < len(lista):
    elemento = lista[i]
    print(elemento)
    i += 1

# Mal uso
for i in range(len(lista)):
    elemento = lista[i]
    print(elemento)

for elemento in lista:
    print(elemento)

# iterables
# Una clase iterable es una clase que puede ser iterada. Dentro de Python hay gran cantidad de clases iterables como las listas, strings, diccionarios o ficheros.
# for elemento in [clase_iterable]:
#   ...

from collections import Iterable

cadena = 'hola'
numero = 3

print('cadena',isinstance(cadena,Iterable))
print('numero',isinstance(numero,Iterable))

# list() convierte a lista una clase iterable
# sum() para sumar
# join() permite unir cada elemento de una clase iterable con el primer argumento usado

print(list('hola'))
print(sum([1,2,3]))
print(".".join('hola'))

# Iteradores
# Se podría explicar la diferencia entre iteradores e iterables usando un libro como analogía. El libro sería nuestra clase iterable, ya que tiene diferentes páginas a las que podemos acceder

libro = ['pagina1','pagina2','pagina3']
marcaPaginas = iter(libro)

# Se va accediendo secuencialmente a los elementos hasta que la excepción StopIteration es lanzada. Dicha excepción se lanza cuando hemos llegado al final, y no existen más elementos que iterar.
print(next(libro))
print(next(libro))
print(next(libro))
