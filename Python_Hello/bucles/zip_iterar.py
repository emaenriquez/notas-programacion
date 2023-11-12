

a = [1,2]
b= ["a","b"]

c = zip(a,b)

print(list(c))

for numero ,texto in zip(a,b):
    print('el numero es',numero,"letra es: ",texto)


numero = [1,2]
espanol = ['uno','dos']
ingles = ['one','two']
frances = ["Un", "Deux"]

for n,e,i,f in zip(numero,espanol,ingles,frances):
    print(n,e,i,f)