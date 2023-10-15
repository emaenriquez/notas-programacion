#listas
listas = ["emanuel","enrui",901,52.21]
#tupla
tupla = ("emanuel","enrui",901,52.21) # no se puede modificar

listas[1] = "batman"

print(listas)
print(tupla)
#--------------------------- creando un conjunto set
# no se puede llamar a sus elementos por su indice y tampoco se puede repetir valores 
conjunto = {"batman","Robin","Red hod","Miles morales","Miles morales"}

print(conjunto)

#--------------------------- creando un diccionario(Dict)

diccionario = {
    # key - value
    'nombre_alumno': 'David',
    'edad': 20,
    'altura': 1.75,
    'estado_civil': 'soltero'
}

print(diccionario["nombre_alumno"])

