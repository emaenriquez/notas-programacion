
def frase(nombre,apellido,adjectivo):
    return f'hola {nombre}{apellido} , sos muy {adjectivo}'

fra = frase("Emanuel","enriquez","Genio")
# utilizando keywords arguments
fra_2 = frase(adjectivo="cap",apellido="Enriquez",nombre="Emanuel")
print(fra_2)

# creando la misma funcion pero con un parametro opcional
def frase_2(nombre,apellido,adjectivo  = 'genio'):
    return f'hola {nombre} , {apellido} soy un {adjectivo}'

palabra_resultante = frase_2('emanuel','enriquez',"cap")

print(palabra_resultante)