
## Apuntes de python

# variables

```python
nombre = "Emanuel"
nombre = 5
nombre = True

# concatenar con string
msj = "Hola " + nombre + " como estas"

# concatenar con f-String
msj = f"Hola {nombre} como estas"

# del msj #operador para borrar datos

print(msj)
#operadores de pertenecica(in , not in)
print("ola" in msj)
print("pedro" not in msj)
```
# tipos de datos 
datos simples
```python
# hola mundo

print("Hola pyton")

"String"
'String'

"""String 
emanuel enriquez"""

'''hola
mundo'''

True
False

3
3.14
```
Dato compuestos
```python
# listas
listas = ["emanuel","enrui",901,52.21]
#tupla
tupla = ("emanuel","enrui",901,52.21) # no se puede modificar

listas[1] = "batman"

print(listas)
print(tupla)
#--------------------------- creando un conjunto set
# no se puede llamar a sus elementos por su indice y tampoco se puede repetir valores 
conjunto = {"batman","Robin","Red hod","Miles morales","Miles morales"}

print(conjunto)

#--------------------------- creando un diccionario(Dict)

diccionario = {
    # key - value
    'nombre_alumno': 'David',
    'edad': 20,
    'altura': 1.75,
    'estado_civil': 'soltero'
}

print(diccionario["nombre_alumno"])
```
# operadores
aritméticos
```python
#suma y resta (+ - )
operacion = 10 + 20
operacion_resta = 20 - 10

# multiplicacion yn division (* y /)
multiplicacion = 12 * 4
division = 3 / 1 # devuelve un dato flotante

#potenciacion (exponente) (**)
exponente = 12**5

#division baja(//)

division_baja = 12//5

#modulo 

modulo = 12%5
```
comparación
```python
es_igual_que = 5 == 6

es_destinto_de = 5!=6

mayor_que = 5 > 8

menor_que = 5 < 8

mayor_o_igual = 5 >=6

menor_o_igual = 5 <= 6
```
Logicos
```python
#AND
resultado = True & True # true
resultado = False & True # falso
resultado = True & False # falso
resultado = False & False # falso
#Or
resultado = True | True # True
resultado = False | True # True
resultado = True | False # True
resultado = False | False # false
#not
resultado = not True #falso
resultado = not False # true
```
# condicionales
```python
numero = 10

if numero >= 10:
    print("el numero es mayor o igual a 10")
elif numero <= 10:
    print("el numero es menor que 10")
else:
    print("el numero no es ni menor ni mayora 10")
```
# metodo de cadena
```python
cadena = "hola,soy,Enriquez"
cadena_2 = "Emanuel"

resultado = dir(cadena)

# convierte a mayusculas
convierte_a_mayusculas = cadena.upper() 

# convierte a minusculas
convierte_a_minusculas = cadena.lower() 

# convierte la primera en mayuscula
convierta_la_primera_letra_mayuscula = cadena.capitalize() 
#buscamos una cadena en otra cadena y nos devuelve la posicion 
#-1 si no encuentra la posicion
busqueda_find = cadena.find("hola")

#buscamos una cadena en otra cadena y nos devuelve la posicion sino encuentra la cadena 
#devuelve un error
busqueda_index = cadena.index("hola")

# si es numerico devolvemos true
es_numerico = cadena.isnumeric()

# si es alfanumerico devovemos true
es_alfanumero = cadena.isalpha()

#count devuelve el numero de ocurrencias de una subcadena en la cadena dada
cadena_conicidencia = cadena.count("o")

#Len cuenta los caracteres de una cadena
caracteres = len(cadena)

#verificamos si una cadena empieza con otra cadena dada,si es asi devuelve true
empieza_con = cadena.startswith("h")

#verificamos si una cadena termina con otra cadena dada,si es asi devuelve true
termina_con = cadena.endswith("y")

#remplazar un valor 
remplazar_cadena = cadena.replace("hola","puto")

# separa cadenas con la cadena que le pasemos
cadena_separada = cadena.split(",")
print(cadena_separada)
```
# metodo de diccionario
```python
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
```
# metodo de lista
```python
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
```
# entrada de datos
```python
#pedirle un dato al usuario

nombre = input("dime tu nombre ")

print(f'tu nombre es: {nombre}')

numero = input("dame un numero ")

# resultado = int(numero) * 2

resultado = float(numero) * 2

print(resultado)
```
# variables 2.0
## conjunto
```python
#creando un conjunto con set
conjunto = set(["dato1"])

#metiendo conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}
# print(conjunto2)

#teoria de conjunto
conjunto1  = {1,2,3,4}
conjunto2 = {2,3,4}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 >= conjunto1

#verificamos si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)
```
## Desempaquetado de variables
```python
#creando datos
datos_tupla = ("Emanuel","Enriquez")
datos_lista = ["Emanuel","Enriquez"]

#desempaquetado
nombre,apellido = datos_lista

print(nombre)
```
## diccionarios
```python
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
```
## tupla
```python
#creando una tupla con tuble()
tupla = tuple(["dato1","dato2"])
#crando una tupla sin parentesis y con multiples datos
tupla = 'dato1','dato2'
#creando una tupla sin parentesis y con un solo valor
tupla = 'dato1',
print(tupla)
```
# bucles 
## while
```python
contador = 1

while contador < 10:
    print(contador)
    contador += 1
```
## iterar un diccionario
```python
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
```
## iterar elementos
```python
# todo funciona igual para las tuplas y listas
animales = ["perro","gato","coodrilo"]
numeros = [1,2,3]
for animal in animales:
    print(animal)

for numero in numeros:
    resultado = numero * 10
    print(resultado)

#recorriendo dos listas al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")

for num in range(5,10):
    print(num)

# forma incorrecta de iterar una lista no funciona en conjunto
for num in range(len(numeros)):
    print(numeros[num])

# forma correcta de iterrar una lista
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"su indice es: {indice} y su respectivo valor es: {valor}")

# usando for con el else
for num in numeros:
    print(f"los valors del ultimo bucle es:{num}")
else:
    print("el bucle termino")
```
## mas iteraciones
```python
frutas = ["banana","Manzana","pera","Mandarina"]
str = "Hola Mundo"
numeros = [1,2,21,2,1,1,2,1]
for fruta in frutas:
    if fruta == 'pera':
        continue
    print(f'las frutas son: {fruta}')

for fruta in frutas:
    if fruta == 'Manzana':
        break
    print(f'las frutas son: {fruta}')

for letra in str:
    print(letra)

#for en una linea de codigo
numeros_duplicados = [x*2 for x in numeros]

print(numeros_duplicados)
```
# funciones
## Crear funciones
```python
#funciones simple
def saludar():
    print("Hola mundo")

# funcion con parametros
def suma (a,b):
    print(a+b)

def saludar_nombre(nombre):
    print(f"Hola {nombre} como estas")

saludar()
suma(10,10)

saludar_nombre("Emanuel")

# crear una funcion que no retorne valores
def password_random(numero):
    lista_de_caracteres = "abdcefghjk"
    numero_entero = str(numero)
    numero = int(numero_entero[0])
    c1 = numero - 2
    c2 = numero
    c3 = numero - 5
    password = f'{lista_de_caracteres[c1]}{lista_de_caracteres[c2]}{lista_de_caracteres[c3]}{numero*2}'
    return password,numero

password ,primer_numero= password_random(2)

msj_password= f"tu contraseña nueva es: {password}"
num_primer= f"tu contraseña nueva es: {primer_numero}"

print(msj_password)
print(num_primer)
```
## Parámetros args
```python
#lo mismo pero utilizamos el operador * como argumento(args)
def suma(*numero):
    return sum(numero)

res = suma(2,3,4,7,9,4,23,7,8,9,4)

print(res)
#  forma obtima 
def suma_total(numero):
    return sum([*numero])
res = suma_total([2,3,4,7,9,4,23,7,8,9,4])
print(res)
```
## Funciones Integradas
```python
lista_numero = {1,2,3,1,2,4,5,62,}

#saber el numero maximo de una lista
numero_max = max(lista_numero)
print(numero_max)

#saber el numero minimo de una lista
numero_min = min(lista_numero)
print(numero_min)

# round
numero =round(12.312121,2)
print(numero)

# retorna false -> 0 , vacio,false,none
res =bool()
print(res)

# retorna true si todos loselementos son verdaderos
resultado_all = all([1,2,31,31,41,2,1,"True",[1,2,21,12]])

#suma todos los valores de un iterable
suma_total = sum(lista_numero)

print(suma_total)
```
## Funciones Extra
```python
def frase(nombre,apellido,adjectivo):
    return f'hola {nombre}{apellido} , sos muy {adjectivo}'

fra = frase("Emanuel","enriquez","Genio")
# utilizando keywords arguments
fra_2 = frase(adjectivo="cap",apellido="Enriquez",nombre="Emanuel")
print(fra_2)

# creando la misma funcion pero con un parametro opcional
def frase_2(nombre,apellido,adjectivo  = 'genio'):
    return f'hola {nombre} , {apellido} soy un {adjectivo}'

palabra_resultante = frase_2('emanuel','enriquez',"cap")

print(palabra_resultante)
```
## Funciones Lamdan
```python
lista = [1,2,3,4,5,6,67,8,9,0,10]

#creando una funcion lambda
multiplicar_por_dos = lambda x : x *2

#funcion que dice si es par o no

def es_par(num):
    if(num % 2 == 0):
        return True;

# usando filter con una funcion comun
numeros_pares = filter(es_par,lista)


#lo mismo que arriba
numeros_pars_2 = filter(lambda numero:numero % 2 == 0,lista)


print(multiplicar_por_dos(10))
print(list(numeros_pares))
print(list(numeros_pars_2))
```
# modulos
```python
# importando un modoulo y le asignamos un nombre
# import modulo_saludar as m_saludar

# desde ese modulo importamos dos funciones
# from modulo_saludar import * importamos todas funciones de ese modulo
# from modulo_saludar import saludar,sumar

# importamos un modulo cuando esta dentro de una carpeta nombre_carpeta.modulo si esta en la misma
# ruta
from funciones_modulos.saludar import saludar , sumar

# llavamos a la funciones y se la asignamos a las varibles
saludo = saludar("David")
res = sumar(10,20)
# mostramos el resultado de las funciones
print(saludo)
print(res)
```
# archivos txt
## leer el archivo con with 
```python
# habriendo archivos con with open
with open('txt\\hola.txt',encoding='UTF-8') as archivo:
    contenido = archivo.read()
    print(contenido)

# no es necesesario cerrar el archivo
```
## Leer el archivo
```python
txt = open('txt\\hola.txt',encoding='UTF-8')

# archivo = txt.read() # para leer un archivo txt

linea_1 = txt.readline() # leer primera linea
lineas = txt.readlines() # leer linea por linea

txt.close() # cierra el archivo
```
## Sobre escribir el archivo
```python
with open('txt\\hola.txt','w',encoding='UTF-8') as archivo:
    #sobre escribiendo el archivo
    # archivo.write('sobre escribiendo')
    archivo.writelines([' Hola ',' Como estas\n ',' todo bien '])
```
## Escribir en el archivo
```python
with open('txt\\hola.txt','a',encoding='UTF-8') as archivo:
    #agregando texto al archivo usando un bucle
    for i in range(5):
        archivo.write(f'los numero son: {i}\n')
```
