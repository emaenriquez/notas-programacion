
# Decoradores
# Los decoradores son funciones que modifican el comportamiento de otras funciones, ayudan a acortar nuestro código

def mi_decorador(funcion):
    def nueva_funcion(a,b):
        print('se va a llamar')
        c = funcion(a,b)
        print('se a llamado')
        return c
    return nueva_funcion

@mi_decorador
def suma(a,b):
    print('entra a la funcion suma')
    return a + b

@mi_decorador
def resta(a,b):
    print('entra a al funcino resta')
    return a - b 

suma(5,8)


