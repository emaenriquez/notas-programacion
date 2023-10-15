
frutas = ["banana","Manzana","pera","Mandarina"]
str = "Hola Mundo"
numeros = [1,2,21,2,1,1,2,1]
for fruta in frutas:
    if fruta == 'pera':
        continue
    print(f'las frutas son: {fruta}')


for fruta in frutas:
    if fruta == 'Manzana':
        break
    print(f'las frutas son: {fruta}')

for letra in str:
    print(letra)
#for en una linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)