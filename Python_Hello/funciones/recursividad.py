# La recursividad o recursión es un concepto que proviene de las matemáticas, y que aplicado al mundo de la programación nos permite resolver problemas o tareas donde las mismas pueden ser divididas en subtareas cuya funcionalidad es la misma


def factoria_normal(n):
    r = 1
    i = 2 
    while i <= n:
        r *= i
        i += 1
    return r

print(factoria_normal(5))

def factoria_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factoria_recursivo(n-1)

print(factoria_recursivo(5))


def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + factoria_recursivo(n-2)