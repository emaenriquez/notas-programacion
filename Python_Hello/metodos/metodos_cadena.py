cadena = "hola,soy,Enriquez"
cadena_2 = "Emanuel"

resultado = dir(cadena)
# convierte a mayusculas
convierte_a_mayusculas = cadena.upper() 
# convierte a minusculas
convierte_a_minusculas = cadena.lower() 
# convierte la primera en mayuscula
convierta_la_primera_letra_mayuscula = cadena.capitalize() 
#buscamos una cadena en otra cadena y nos devuelve la posicion -1 si no encuentra la posicion
busqueda_find = cadena.find("hola")
#buscamos una cadena en otra cadena y nos devuelve la posicion sino encuentra la cadena 
#devuelve un error
busqueda_index = cadena.index("hola")

# si es numerico devolvemos true
es_numerico = cadena.isnumeric()
# si es alfanumerico devovemos true
es_alfanumero = cadena.isalpha()

#count devuelve el numero de ocurrencias de una subcadena en la cadena dada
cadena_conicidencia = cadena.count("o")
#Len cuenta los caracteres de una cadena
caracteres = len(cadena)

#verificamos si una cadena empieza con otra cadena dada,si es asi devuelve true
empieza_con = cadena.startswith("h")
#verificamos si una cadena termina con otra cadena dada,si es asi devuelve true
termina_con = cadena.endswith("y")

#remplazar un valor 
remplazar_cadena = cadena.replace("hola","puto")

# separa cadenas con la cadena que le pasemos
cadena_separada = cadena.split(",")
print(cadena_separada)