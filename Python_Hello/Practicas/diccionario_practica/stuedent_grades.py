# Student Grades
# Create a dictionary that maps student names to a list of their grades. Implement functions to add a new student with their grades, remove a student, calculate the average grade for a given student, and determine the highest and lowest grade for each student.


student_grades = {}

def add_new_student(name,lengua,mate,fisica,ciencias_sociales):
    student_grades[name]={
        'lengua': lengua,
        'matematica': mate,
        'fisica': fisica,
        'ciencias_sociales': ciencias_sociales
    }

def promedio_student(notas):
    total_notas = sum(notas.values())
    promedio = total_notas /len(notas)
    return promedio

def mostrar_promedio():
    for estudiante,notas in student_grades.items():
        promedio = promedio_student(notas)
        print(f'promedio del estudiante {estudiante} {promedio: .2f}')

def remove_student(name):
    if name in student_grades:
        del student_grades[name]

def nota_mas_alta(notas):
    notas_alta = max(notas.values())
    return notas_alta

def nota_mas_baja(notas):
    notas_min = min(notas.values())
    return notas_min

def mostrar_nota_alta_baja():
    for estudiante,nota in student_grades.items():
        mas_alta = nota_mas_alta(nota)
        mas_baja = nota_mas_baja(nota)
        print(f'la nota mas alta de {estudiante} es: {mas_alta}')
        print(f'la nota mas baja de {estudiante} es: {mas_baja}')

add_new_student("Matias",1,10,2,3)
add_new_student("Fernanda",10,2,3,7)
add_new_student("Habril",7,3,6,10)

print(student_grades)

mostrar_promedio()
mostrar_nota_alta_baja()