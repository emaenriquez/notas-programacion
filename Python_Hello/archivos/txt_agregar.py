
with open('archivos\\hola.txt','a',encoding='UTF-8') as archivo:
    #agregando texto al archivo usando un bucle
    for i in range(5):
        archivo.write(f'los numero son: {i}\n')
    