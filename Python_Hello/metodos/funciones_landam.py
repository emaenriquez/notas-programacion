
lista = [1,2,3,4,5,6,67,8,9,0,10]

#creando una funcion lambda
multiplicar_por_dos = lambda x : x *2

#funcion que dice si es par o no

def es_par(num):
    if(num % 2 == 0):
        return True;

# usando filter con una funcion comun
numeros_pares = filter(es_par,lista)


#lo mismo que arriba
numeros_pars_2 = filter(lambda numero:numero % 2 == 0,lista)


print(multiplicar_por_dos(10))
print(list(numeros_pares))
print(list(numeros_pars_2))
