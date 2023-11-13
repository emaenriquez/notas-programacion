

# Patrones de diseño 

soluciones generales y reutilizables para problemas comunes que los desarrolladores enfrentan al diseñar software. 

## clasificacion de los patrones de diseño

## patrones creacionales

se encargar de aquellos que solucionan donde implica crear crear obj
su  objectivo es dar soluciones para poder dar instancias complejas de sierto obj

### Factory
```python 
# Definición de la clase base para los personajes
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

    def atacar(self):
        pass

# Definición de las subclases de personajes
class Guerrero(Personaje):
    def atacar(self):
        return f"{self.nombre} ataca con su espada."

class Mago(Personaje):
    def atacar(self):
        return f"{self.nombre} lanza un hechizo mágico."

# Definición de la fábrica de personajes
class FabricaPersonajes:
    def crear_personaje(self, nombre, tipo):
        if tipo == "guerrero":
            return Guerrero(nombre)
        elif tipo == "mago":
            return Mago(nombre)
        else:
            raise ValueError(f"Tipo de personaje no válido: {tipo}")

# Uso del patrón Factory Method
fabrica = FabricaPersonajes()

personaje1 = fabrica.crear_personaje("Aragorn", "guerrero")
personaje2 = fabrica.crear_personaje("Gandalf", "mago")

print(personaje1.atacar())  # Salida: Aragorn ataca con su espada.
print(personaje2.atacar())  # Salida: Gandalf lanza un hechizo mágico.

```
### Abstract Factory
patron de diseño que provee una interficie para crear familias de objetos relacionados o dependientes sin especificar su
clase concreta , te permite crear objetos que siguen un cierto tema o conjunto de características comunes sin preocuparte por las clases exactas de esos objetos.
```python
# Definición de la interfaz Abstract Factory
class PersonajeFactory:
    def crear_personaje(self):
        pass

    def crear_equipo(self):
        pass

# Implementación concreta de la fábrica para personajes guerreros
class FabricaGuerreros(PersonajeFactory):
    def crear_personaje(self):
        return Guerrero()

    def crear_equipo(self):
        return EquipoGuerrero()

# Implementación concreta de la fábrica para personajes magos
class FabricaMagos(PersonajeFactory):
    def crear_personaje(self):
        return Mago()

    def crear_equipo(self):
        return EquipoMago()

# Clases concretas de personajes y equipos
class Guerrero:
    def habilidad(self):
        return "Atacar con espada"

class Mago:
    def habilidad(self):
        return "Lanzar hechizos"

class EquipoGuerrero:
    def descripcion(self):
        return "Equipo de guerrero: Espada y armadura pesada"

class EquipoMago:
    def descripcion(self):
        return "Equipo de mago: Varita y túnica"

# Uso del patrón Abstract Factory
def crear_personaje_y_equipo(factory):
    personaje = factory.crear_personaje()
    equipo = factory.crear_equipo()
    return personaje, equipo

fabrica_guerreros = FabricaGuerreros()
fabrica_magos = FabricaMagos()

personaje1, equipo1 = crear_personaje_y_equipo(fabrica_guerreros)
personaje2, equipo2 = crear_personaje_y_equipo(fabrica_magos)

print("Personaje 1:", personaje1.habilidad(), "con", equipo1.descripcion())
print("Personaje 2:", personaje2.habilidad(), "con", equipo2.descripcion())

```
### Builder

## Pattones estructurales
nos ayuda a la hora de configurar relaciones entre obj 

### Composide

## Patrones de comportamiento
son utilizados para gestionar las relaciones y las interacciones entre objetos en una aplicación. Estos patrones se centran en cómo los objetos colaboran y comunican entre sí para lograr un comportamiento específico.
 
### Strategy
El patrón Strategy permite que el cliente elija el algoritmo apropiado en tiempo de ejecución, sin cambiar la estructura del código. Esto promueve la flexibilidad y la modularidad en el diseño de software

```python
# Definición de la interfaz de la estrategia
class EstrategiaImpuesto:
    def calcular_impuesto(self, ingresos):
        pass

# Implementación de las estrategias concretas
class ImpuestoSobreLaRenta(EstrategiaImpuesto):
    def calcular_impuesto(self, ingresos):
        return ingresos * 0.25  # Simulación de cálculo de impuesto sobre la renta

class ImpuestoSobreVentas(EstrategiaImpuesto):
    def calcular_impuesto(self, ingresos):
        return ingresos * 0.10  # Simulación de cálculo de impuesto sobre ventas

# Contexto que utiliza una estrategia
class CalculadoraImpuestos:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def calcular(self, ingresos):
        return self.estrategia.calcular_impuesto(ingresos)

# Uso del patrón Strategy
estrategia_renta = ImpuestoSobreLaRenta()
estrategia_ventas = ImpuestoSobreVentas()

calculadora1 = CalculadoraImpuestos(estrategia_renta)
calculadora2 = CalculadoraImpuestos(estrategia_ventas)

ingresos1 = 100000
ingresos2 = 50000

impuesto1 = calculadora1.calcular(ingresos1)
impuesto2 = calculadora2.calcular(ingresos2)

print(f"Impuesto sobre la renta: ${impuesto1}")
print(f"Impuesto sobre ventas: ${impuesto2}")
```