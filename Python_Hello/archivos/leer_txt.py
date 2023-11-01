
txt = open(r"C:\Users\Usuario\Documents\notas_programacion\Python_Hello\archivos\hola.txt",encoding='UTF-8')

# archivo = txt.read() # para leer un archivo txt

linea_1 = txt.readline() # leer primera linea
lineas = txt.readlines() # leer linea por linea

txt.close() # cierra el archivo

