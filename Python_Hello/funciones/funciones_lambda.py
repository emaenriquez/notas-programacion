

# Funciones lambda
# Las funciones lambda o anónimas son un tipo de funciones en Python que típicamente se definen en una línea y cuyo código a ejecutar suele ser pequeño.


def suma(a,b):
    return a + b

lambda a,b : a + b 

# Ejemplos
# Una función lambda puede ser la entrada a una función normal

def miFuncion(lambda_fucion):
    return lambda_fucion(2,4)

miFuncion( lambda a,b : a + b )