
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

password = "contraseña"

password_get_usuario = input('ingrese contraseña')

while True:
    if password == password_get_usuario:
        print('la contraseña es correcta')
        break
    else:
        print('la contraseña es incorrecta ingresela de vuelta')
        password_get_usuario = input('ingrese contraseña')