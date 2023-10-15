
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input('ingrese su edad para saber si tiene que tributar un determinado impuesto'))
ingreso_mensuales = float(input('ingrese su ingresos mensuales'))

if edad > 16 and ingreso_mensuales > 1000:
    print('usted tiene que tributar el impuesto')
else:
    print('usted no debe tramitar este impuesto')