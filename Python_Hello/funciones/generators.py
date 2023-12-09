
# Generators en Python
# la función devuelve el control a quién la llamó, pero la función es pausada y el estado (valor de las variables) es guardado
def funcion():
    return 5

def generador():
    yield 5

print(funcion())
print(generador())

# Iterando los Generadores
# sólo tenemos una llamada a yield.
a = generador()
print(next(a)) # Salida: 5
# print(next(a)) # Salida: Error! StopIteration:

# Creando Generadores

def generador_1():
    n = 1
    yield n 
    
    n += 1
    yield n

    n += 1
    yield n  

for i in generador_1():
    print(i)


# Forma alternativa
# Los generadores también pueden ser creados de una forma mucho más sencilla y en una sola línea de código.

lista = [2,4,6,8,10]

al_cuadrado  = [x**2 for x in lista]

print(al_cuadrado)


def primerosNumeros(n):
    nums = []
    for i in range(n):
        nums.append(i)
    return nums

print(sum(primerosNumeros(100)))

def primerosNumeros2(n):
    nums = 0
    for i in range(n):
        yield nums
        nums += 1
print(sum(primerosNumeros2(100)))