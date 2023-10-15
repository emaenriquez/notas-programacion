# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

# lista_numero = []

# for i in range(11):
#     lista_numero.append( int( input('ingrese 10 numeros') ) )
# lista_numero.reverse()

# print('los numeros en orden inverso son ' + str(lista_numero))

lista_numero = [1,2,3,4,5,6,7,8,9,10]

for i in lista_numero:
    print(lista_numero[-i], end=", ")
