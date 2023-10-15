
#funciones simple
def saludar():
    print("Hola mundo")

# funcion con parametros
def suma (a,b):
    print(a+b)

def saludar_nombre(nombre):
    print(f"Hola {nombre} como estas")

saludar()
suma(10,10)

saludar_nombre("Emanuel")

# crear una funcion que no retorne valores
def password_random(numero):
    lista_de_caracteres = "abdcefghjk"
    numero_entero = str(numero)
    numero = int(numero_entero[0])
    c1 = numero - 2
    c2 = numero
    c3 = numero - 5
    password = f'{lista_de_caracteres[c1]}{lista_de_caracteres[c2]}{lista_de_caracteres[c3]}{numero*2}'
    return password,numero

password ,primer_numero= password_random(2)

msj_password= f"tu contraseña nueva es: {password}"
num_primer= f"tu contraseña nueva es: {primer_numero}"

print(msj_password)
print(num_primer)