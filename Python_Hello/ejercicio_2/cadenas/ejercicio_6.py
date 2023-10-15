# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.


str_frase = input("ingrese una frase ")
str_vocal = input("ingrese una vocal ")

def frase(cadena,vocal):
    cadena_modificada = cadena.replace(vocal,vocal.upper())
    print(cadena_modificada)


frase(str_frase,str_vocal)
