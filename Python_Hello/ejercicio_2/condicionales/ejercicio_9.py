
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.


edad_cliente = int(input('ingrese su edad y se mostrara el precio de la entrada '))

if edad_cliente < 4:
    print('usted entra gratis')
elif edad_cliente < 18:
    print('tiene que pagar 5€')
else:
    print('tiene que pagar 10€')




