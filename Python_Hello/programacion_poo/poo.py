
# Programación Orientada a Objetos
# las clases Estas nos permiten agrupar un conjunto de variables y funciones
# atributos diferentes caracteristicas de las clases
# metodos cosas que puede hacer la clase (funciones)

# La programación orientada a objetos está basada en 6 principios o pilares básicos:
    # Herencia
    # Cohesión
    # Abstracción
    # Polimorfismo
    # Acoplamiento
    # Encapsulamiento

class Perro:
    pass

# Creamos un objeto de la clase perro
mi_perro = Perro()

# Definiendo atributos
# A continuación vamos a añadir algunos atributos a nuestra clase
    # Atributos de instancia: Pertenecen a la instancia de la clase o al objeto. 
    # Atributos de clase: Se trata de atributos que pertenecen a la clase

class Perro:
    # Atributo de clase
    especie = 'mamífero'

    # El método __init__ es llamado al crear el objeto
    def __init__(self,nombre,raza):
        print(f'creano perro {nombre}, {raza}')
    
        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza

mi_perro = Perro('toni','Bulldog')

print(mi_perro.nombre)
print(mi_perro.raza)
print(mi_perro.especie)


# Definiendo métodos
# En realidad cuando usamos __init__ anteriormente ya estábamos definiendo un método,

class Perro:
    # Atributo de clase
    especie = 'mamífero'

    # El método __init__ es llamado al crear el objeto
    def __init__(self,nombre,raza):
        print(f'creano perro {nombre}, {raza}')
    
        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza
    # self hace referencia a la instancia de la clase.
    def labra(self):
        print('guau')
    def camina(self,pasos):
        print(f'lo pasos son {pasos}')

mi_perro = Perro('toni','Bull')

mi_perro.camina(10)