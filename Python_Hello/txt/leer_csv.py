
import csv
with open("txt\\anexo4.csv") as archivo:
    # print(csv.reader(archivo))
    reader = csv.reader(archivo)
    for row in reader:
        print(row)
    # print(archivo.read())