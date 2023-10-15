
# importando un modoulo y le asignamos un nombre
# import modulo_saludar as m_saludar

# desde ese modulo importamos dos funciones
# from modulo_saludar import * importamos todas funciones de ese modulo
# from modulo_saludar import saludar,sumar

# importamos un modulo cuando esta dentro de una carpeta nombre_carpeta.modulo si esta en la misma
# ruta
from funciones_modulos.saludar import saludar , sumar

# llavamos a la funciones y se la asignamos a las varibles
saludo = saludar("David")
res = sumar(10,20)
# mostramos el resultado de las funciones
print(saludo)
print(res)


