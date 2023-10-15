

lista = [1,20,21,1,2,21,1,1,1,12,2,2,2,1,1]

tuplas = (1,2,3,1,2,4,2,21,)

cojunto = {5,6,7,8,9,10,11,11,}


diccioario = {
    'a':'abecede',
    'b':'becede'
}


# cadena = input(" ingresa una cadena ")

# concurencia = cadena.count('E')

# for caracter in cadena:
#     concurencia = cadena.count(caracter)
#     print(f' las concurencias son: {caracter} aparercio: {concurencia}')


# Contador de Palabras: Crea una función que cuente cuántas palabras hay en una oración.


def contador_palbras(str):
    cadena = str.split()
    cantidad_de_palabras = len(cadena)
    print(cantidad_de_palabras)

contador_palbras("Emanuek enriquez")


# Eliminación de Espacios en Blanco: Escribe una función que tome una cadena y elimine todos los espacios en blanco.


def eleminar_espacio_blanco(str):
    cadena = str.replace(" ","")
    print(cadena)

eleminar_espacio_blanco("emanuel eneurqa")


# Mayúsculas y Minúsculas: Escribe un programa que tome una cadena como entrada y la imprima en mayúsculas y minúsculas.

def entrada(str):
    cadena_mayuscula = str.upper()
    cadena_minuscula = str.lower()
    print(f"{cadena_mayuscula} + {cadena_minuscula}")

entrada("emanuel")

# Reemplazo de Subcadena: Crea una función que tome una cadena, una subcadena y una cadena de reemplazo, y reemplace todas las ocurrencias de la subcadena con la cadena de reemplazo.


def remplazo_cadena(cadena,subcadena,cadena_remplazo):
    cadena_nueva = cadena.replace(subcadena,cadena_remplazo)
    print(cadena_nueva)

remplazo_cadena("Python es genial y Python es divertido","Python","java")    



# Validación de Contraseña: Escribe un programa que verifique si una contraseña cumple con ciertos requisitos, como tener al menos una letra mayúscula, un número y una longitud mínima.

def tiene_mayuscula(cadena):
    for caracter in cadena:
        if caracter.isupper():
            return True
    return False

def validacion_password(password):
    m = tiene_mayuscula(password)
    print(m)
    if(len(password) > 10 & tiene_mayuscula(password)):
        print("la password es aceptada")
    else:
        print("la password no tiene una longitud mayor 10 inglesela nueva mente")

validacion_password("spid")


# Formato de Nombres: Escribe una función que tome un nombre en formato "apellido, nombre" y lo convierta en "nombre apellido".

def formato_nombre(apellido,nombre):
    print(f'Hola soy {nombre} {apellido}')
