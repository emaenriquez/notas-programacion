
#  son secuencias de caracteres que conforman un patrón de búsqueda. En Python, se pueden utilizar para realizar operaciones de búsqueda y sustitución en cadenas de texto.
import re

# Compilamos la expresión regular
patron = re.compile('ab+c')
patron = re.compile('a.b*')

# Probamos la expresión regular con una cadena de texto
texto = 'abc'

# Realizamos la búsqueda
coincidencia = patron.match(texto)

# Comprobamos si hubo una coincidencia
if coincidencia:
    print('Se encontró una coincidencia')
else:
    print('No se encontró ninguna coincidencia')