#lo mismo pero utilizamos el operador * como argumento(args)
def suma(*numero):
    return sum(numero)

res = suma(2,3,4,7,9,4,23,7,8,9,4)

print(res)
#  forma obtima 
def suma_total(numero):
    return sum([*numero])
res = suma_total([2,3,4,7,9,4,23,7,8,9,4])
print(res)