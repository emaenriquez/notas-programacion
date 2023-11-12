class Pato:
    def Hablar(self):
        print('cual,cual')

class Perro:
    def Hablar(self):
        print('guau,guau')

class Gato:
    def Hablar(self):
        print('miua,miau')

class Vaca:
    def Hablar(self):
        print('muuuuuu')

pato = Pato()
perro = Perro()
gato = Gato()
vaca = Vaca()


pato.Hablar()

def llamar_hablar(x):
    x.Hablar()

llamar_hablar(pato)
llamar_hablar(perro)
llamar_hablar(gato)
llamar_hablar(vaca)

lista = [Perro(),Gato(),Vaca()]

for animal in lista:
    print(animal)


class Foo:
        def __len__(self):
            return 99

class Bar():
    pass

print(len(Foo())) # 99
# print(len(Bar())) # error

print(3*3)
print(3*'3')