
import csv
with open(r"C:\Users\Usuario\Documents\notas_programacion\Python_Hello\archivos\datos.csv") as archivo:
    # print(csv.reader(archivo))
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
    # print(archivo.read())