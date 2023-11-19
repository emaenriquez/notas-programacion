

# las list comprehension nos permiten crear listas de elementos en una sola línea de código.
# lista = [expresión for elemento in iterable]
cuadrados = [i**2 for i in range(5)]
print(cuadrados)

valor_constante = [1 for i in range(5)]

print(valor_constante)

# La expresión también puede ser una llamada a una función

def elevado_2(i):
    return i**2

cuadrados_2 = [elevado_2(i) for i in range(5)]

print(cuadrados_2)

# Cualquier elemento que sea iterable puede ser usado con las list comprehensions. 

lista_numero = [10,20,30,40,50]

nueva_lista = [i/10 for i in lista_numero]

print(nueva_lista)

# Añadiendo condicionales
# lista = [expresión for elemento in iterable if condición]

frase = "El perro de san roque no tiene rabo"

erres = [i for i in frase if i == 'r']

print(erres)

pares = [i for i in range(6) if i % 2 == 0]

print(pares)

# Sets comprehension

mi_set = {i for i in frase if i=='r'}
print(mi_set)

# Dictionary comprehension

lista1 = ['nombre', 'edad', 'región']
lista2 = ['Pelayo', 30, 'Asturias']

mi_dict = {i:j for i ,j in zip(lista1,lista2)}

print(mi_dict)