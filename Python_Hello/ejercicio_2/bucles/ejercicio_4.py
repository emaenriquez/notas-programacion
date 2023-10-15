
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input('ingrese numero'))

# contador = 10

while numero >= 0:
    print(f"{numero}", end=', ')
    numero -= 1