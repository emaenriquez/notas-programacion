# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo_electronico = 'emadominguez1985@gmail.com'

otro_correo = correo_electronico.replace('@gmail.com','@ceu.es')

print(correo_electronico)
print(otro_correo)