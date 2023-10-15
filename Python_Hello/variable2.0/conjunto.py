#creando un conjunto con set
conjunto = set(["dato1"])

#metiendo conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}
# print(conjunto2)

#teoria de conjunto
conjunto1  = {1,2,3,4}
conjunto2 = {2,3,4}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 >= conjunto1

#verificamos si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)
