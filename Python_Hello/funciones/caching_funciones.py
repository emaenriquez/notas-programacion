
from functools import lru_cache


# Caching de Funciones
# El caché es un término muy usado en informática, y hace referencia al almacenamiento de resultados previos para su posterior reutilización, lo que permite reducir el tiempo de respuesta

# cache miss se almacena por si fuera útil en el futuro
# cache hit la caché tiene almacenado el resultado para esa operación, en vez de calcular otra vez la salida la podemos reutilizar

def es_primo(num):
    for n in range(2,num):
        if num % n == 0:
            return False
    return True

# Caching con Diccionarios

def es_primo_concache(num,_cache={}):
    if num not in _cache:
        _cache[num] = True
        for n in range(2,num):
            if num % n == 0:
                _cache[num] = False
                break
    return _cache[num]

# Caching con functools y lru_cache

@lru_cache(maxsize=32)
def es_primo_concache(num):
    for n in range(2,num):
        if num % n == 0:
            return False
    return True