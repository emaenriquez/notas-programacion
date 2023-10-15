

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.


asignatura_curso = list(["Matemáticas", "Física", "Química", "Historia", "Lengua"])

for lista in asignatura_curso:
    print(f'yo estudio {lista}')