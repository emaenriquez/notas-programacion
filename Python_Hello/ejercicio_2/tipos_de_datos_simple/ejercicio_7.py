# Ejercicio 7
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso_usuario = input("ingrese su peso en kg")
estatura_metros = input("ingrese su estatura en metros")

imc = round( float(peso_usuario) / float(estatura_metros) ** 2,2)

print(f"su indice de masa corporal es:{imc} ")