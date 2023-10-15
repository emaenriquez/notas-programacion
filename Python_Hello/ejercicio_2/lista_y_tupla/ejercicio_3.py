
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

asignatura_curso = list(["Matemáticas", "Física", "Química", "Historia", "Lengua"])
nota = []
for lista in asignatura_curso:
    notas = input(f'que nota has sacado en {lista}')
    nota.append(notas)

for i in range(len(asignatura_curso)):
    print(f'en la {asignatura_curso[i]} has sacado {nota[i]}')


