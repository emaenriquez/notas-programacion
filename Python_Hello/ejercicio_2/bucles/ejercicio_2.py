
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


age = int(input('ingrese su edad'))

for i in range(age):
    print('has cumplido '+ str(i+1) + ' años')