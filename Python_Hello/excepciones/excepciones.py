

# creando la funacion suma
def sumar():
    # iniciando bucle
    while True:
        # pidiendo numeros
        num1 = input('numero 1: ')
        num2 = input('numero 2: ')
        # conviritendo numero esteros y sumarlos
        try:
            res = int(num1) + int(num2)
        # pedirle de nuevo los numero si lanza un excepcion
        except:
            print('por favor no te detengas')
        # si todo salio bien terminamos el bucle
        else:
            break
        finally:
            print('esto se ejecuta siempre')
    return res

print(sumar())