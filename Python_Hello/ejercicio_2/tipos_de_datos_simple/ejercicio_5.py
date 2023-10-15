#  Ejercicio 5
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas_trabajadas = input("la cantidad de horas trabjadas")
coste_por_horas = input("deme su coste por horas")

paga = int(horas_trabajadas) * int(coste_por_horas)
# """"""
print(f"""la cantidad de horas trabajadas son: {horas_trabajadas} y pago por hora es    {coste_por_horas}$ en total de su trabajo es: {paga}$""")
