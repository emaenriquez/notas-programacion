def f(x):
    return 2 * x 

y = f(3)

print(y)

# Pasando argumentos de entrada

def hola():
    print('hola mundo')

def hola_nombre(nombre):
    print('hola',nombre)

hola_nombre('emanuel')

def resta(num1,num2):
    return num1 - num2

# argunmento por defecto
def suma(a,b,c=3):
    return a + b + c

def suma_2(a=1,b=2,c=3):
    return a + b + c

# argumento con logitud variable

def suma(numeros):
    total = 0
    for n in numeros:
        total += n
    return total

# esto hará que el argumento que se pase sea empaquetado en una tupla de manera automática. 
def suma_1(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(suma_1(1,2,3,4,5,6))

# Usando doble ** es posible también tener como parámetro de entrada una lista de elementos almacenados en forma de clave y valor.

def suma_3(**kwargs):
    suma = 0
    for key,value in kwargs.items():
        print(key,value)
        suma += value
    return suma

dic = {'a':10,'b':20}

print(suma_3(a=5,b=10,c=10))

print(suma_3(**dic))

# Paso por valor y referencia
# Si usamos un parámetro pasado por valor, se creará una copia local de la variable, lo que implica que cualquier modificación sobre la misma no tendrá efecto sobre la original.
# Con una variable pasada como referencia, se actuará directamente sobre la variable pasada, por lo que las modificaciones afectarán a la variable original.


# valor

x = 10
def funcion(entrada):
    entrada = 0

funcion(x)

# referencia

x = [10,20,30]

def funcion(entrada):
    entrada.append(40)

funcion(x)

print(x)

# la función id(). Esta función nos devuelve un identificador único para cada objeto

# x = 10
# print(id(x)) # 4349704528
# def funcion(entrada):
#     entrada = 0
#     print(id(entrada)) # 4349704208

# funcion(x)

# Uso de *args
# podemos definir funciones cuyo número de argumentos es variable
def nombre(*args):
    s = 0
    for arg in args:
        s += arg
    return s

# Uso de **kwargs
# los **kwargs nos permiten dar un nombre a cada argumento de entrada
# omo podemos ver, es posible iterar los argumentos de entrada con items(), y podemos acceder a la clave key (o nombre) y el valor o value de cada argumento

def sumacion(**kwargs):
    s = 0
    for key,value in kwargs.items():
        print(key,"=",value)
    return s

def funcion(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    for arg in args:
        print("args =", arg)
    for key, value in kwargs.items():
        print(key, "=", value)

funcion(10, 20, 1, 2, 3, 4, x="Hola", y="Que", z="Tal")
#Salida
#a = 10
#b = 20
#args = 1
#args = 2
#args = 3
#args = 4
#x = Hola
#y = Que
#z = Tal
# Function Annotations en Python
# Las anotaciones en funciones o function annotations de Python nos permiten añadir el tipo de los argumentos de entrada y salida de una función. 

def suma_4(a:int,b:int):
    return a + b

print(suma_4(10,20))


def filtrar_pares(salida: 'list' = []) -> 'list':
    return [i for i in salida if i%2 == 0]

print(filtrar_pares([1, 2, 3, 4, 5, 6]))

pi: float = 3.14
print(pi)

# Uso de mypy y Static Type Checking