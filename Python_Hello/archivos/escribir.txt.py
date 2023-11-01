

with open(r"C:\Users\Usuario\Documents\notas_programacion\Python_Hello\archivos\hola.txt",'w',encoding='UTF-8') as archivo:
    #sobre escribiendo el archivo
    # archivo.write('sobre escribiendo')
    archivo.writelines([' Hola ',' Como estas\n ',' todo bien '])