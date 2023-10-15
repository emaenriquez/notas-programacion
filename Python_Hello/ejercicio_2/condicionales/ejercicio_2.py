# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al
#  usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

key = 'Emanuel'

password = input('ingrese la contraseña')

if key == password.lower():
    print('la contraseña es correcta')
else:
    print('la contraseña no es correcta')