# Ejercicio 10
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.


numero_de_ventas_payaso = input("ingrese la cantidad de payasos vendidos en el ultimo pedido ")
numero_de_ventas_muñecas = input("ingrese la cantidad de muñecas vendidas en el ultimo pedido ")

peso_payasos = 112
peso_muñecas = 75

peso_total = peso_payasos *float( numero_de_ventas_payaso) + peso_muñecas * float(numero_de_ventas_muñecas)

print(f"el peso total del paquete es: {peso_total}g")
