# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

num1 = int(input(' ingrese numero para saber si es par o impar '))

if num1 % 2 == 0:
    print('el numero es par')
else:
    print('el numero es impar')