# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

cadena = input("ingrese una cadena")

def cadena_invertidad(str):
    frase_invertidad = str[::-1]
    print(frase_invertidad)


cadena_invertidad(cadena)