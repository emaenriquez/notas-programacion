# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio_producto = input('ingrese el producto en euro con dos decimales')

print(precio_producto[:precio_producto.find('.')],'euro y',precio_producto[:precio_producto.find('.')+1:],'centimos')
