# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre_usuario = input("ingrese su nombre: ")
numero_entero = input("ingrese un numero entero: ")
numero_entero_2 = int(numero_entero)
contador = 0
while contador < numero_entero_2:
    print(nombre_usuario)
    contador += 1