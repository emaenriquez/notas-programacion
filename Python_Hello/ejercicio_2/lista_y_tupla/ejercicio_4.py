# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

lista = []
for i in range(6):
    lista.append(int(input('ingrese los numeros ganardores de la loteria')))
lista.sort()
print('los numeros ganardores son'  + str(lista))