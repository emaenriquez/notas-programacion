# Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.


nombre_usuario = input("ingrese nombre de completo: ")

print(f"su nombre es: {nombre_usuario.upper()}")
print(f"su nombre es: {nombre_usuario.lower()}")
print(f"su nombre es: {nombre_usuario.title()}")
