
# todo funciona igual para las tuplas y listas
animales = ["perro","gato","coodrilo","swwswef"]
numeros = [1,2,3]
for animal in animales:
    print(animal)

for numero in numeros:
    resultado = numero * 10
    print(resultado)

#recorriendo dos listas al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")

for num in range(5,10):
    print(num)

# forma incorrecta de iterar una lista no funciona en conjunto
for num in range(len(numeros)):
    print(numeros[num])

# forma correcta de iterrar una lista
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"su indice es: {indice} y su respectivo valor es: {valor}")

# usando for con el else
for num in numeros:
    print(f"los valors del ultimo bucle es:{num}")
else:
    print("el bucle termino")