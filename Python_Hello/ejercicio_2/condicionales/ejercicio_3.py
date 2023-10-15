# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

num1 = int(input('ingrese el primer numero: '))
num2 = int(input('ingrese el segundo numero: '))

if(num2 == 0):
    print('Error')
else:
    print(num1 / num2)