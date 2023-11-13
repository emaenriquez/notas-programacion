# Java

# **Modificadores de Acceso**

l**os modificadores de acceso son palabras clave que se utilizan para controlar el alcance de una clase, un método o una variable**

- **`public`**: permite que cualquier clase o método acceda a la variable o método.
- **`private`**: restringe el acceso a la variable o método a solo la clase en la que se declaró. Los métodos y variables privados no pueden ser accedidos desde fuera de la clase en la que se declararon.
- **`protected`**: permite que las subclases y las clases en el mismo paquete accedan a la variable o método.
- **`default`**: no se especifica un modificador de acceso, se entiende como que es accesible desde las clases del mismo paquete.

```java
	public String nombre;
	private String apellido; // Atributos
	String dni;
	**protected String telefono**
```

# **Tipo de datos primitivos**

En Java, hay 8 tipos de datos primitivos:

**int**: es utilizado para almacenar números enteros.

```java
int numero = 10;
```

**float**: es utilizado para almacenar números con decimal flotante.

```java
float decimal = 3.14f;
```

**double**: es utilizado para almacenar números con decimal flotante con precisión doble.

```java
double decimal = 3.14;
```

**char**: es utilizado para almacenar un carácter.

```java
char letra = 'A';
```

**boolean**: es utilizado para almacenar valores lógicos (verdadero o falso). 

```java
boolean verdadero = true;
boolean falso = false;
```

**byte**: es utilizado para almacenar números enteros de 8 bits.

```java
byte numero = 100;
```

**short**: es utilizado para almacenar números enteros de 16 bits.

```java
short numero = 1000;
```

**long**: es utilizado para almacenar números enteros de 64 bits.

```java
long numero = 100000L;
```

**ASIGNACIÓN**: es cuando le damos el valor a un variable que inicializada pero se le a asignado ningún valor

**entrada y salida de la información**:

- los operadores de entrada permiten leer determinados valores y asignarles ese valor a las variables
- los operadores de salida permiten escribir o mostrar el valor de una variable en concreto

# L**os operadores lógico**

los operadores lógicos "and" (&&), "or" (||) y "not" (!) se utilizan para comparar valores booleanos y para combinar expresiones lógicas.

**El operador && (and lógico)** evalúa si dos o más expresiones son verdaderas. Si todas las expresiones son verdaderas, el resultado de la expresión es verdadero, de lo contrario es falso.

**El operador || (or lógico)** evalúa si al menos una de las expresiones es verdadera. Si al menos una expresión es verdadera, el resultado de la expresión es verdadero, de lo contrario es falso.

**El operador ! (not lógico)** Si la expresión es verdadera, el resultado será falso y si la expresión es falsa, el resultado será verdadero.

```java
int x = 5;
int y = 10;
boolean check1 = (x < y) && (y > 0); // resultado: true
boolean check2 = (x > y) || (y < 0); // resultado: false
boolean check3 = !(x == y); // resultado: true

```

# **estructuras de control de flujo**

Java tiene varias estructuras de control de flujo, las cuales se utilizan para controlar el flujo de ejecución de un programa. Algunas de las estructuras de control más comunes en Java son:

**if-else**: esta estructura permite ejecutar un bloque de código si se cumple una condición específica. 

```java
Copy code
if (x > 0) {
   System.out.println("x es mayor que cero");
} else {
   System.out.println("x es menor o igual a cero");
}

```

**switch-case**: esta estructura permite ejecutar un bloque de código específico dependiendo del valor de una variable. Por ejemplo:

```java
int numero = 2;

switch (numero) {
   case 1:
      System.out.println("El número es 1");
      break;
   case 2:
      System.out.println("El número es 2");
      break;
   case 3:
      System.out.println("El número es 3");
      break;
   default:
      System.out.println("El número no es 1, 2 ni 3");
}
```

**for**: esta estructura permite ejecutar un bloque de código varias veces en un bucle. Por ejemplo:

```java
for (int i = 0; i < 10; i++) {
   System.out.println("Iteración: " + i);
}
```

**while**: esta estructura permite ejecutar un bloque de código mientras se cumpla una condición. Por ejemplo:

```java
int x = 10;

while (x > 0) {
   System.out.println("x: " + x);
   x--;
}
```

**do-while**: esta estructura es similar al while, pero asegura que el bloque de código se ejecutará al menos una vez. Por ejemplo:

```java
int x = 10;

do {
   System.out.println("x: " + x);
   x--;
} while (x > 0);

```

**break, continue**: estas palabras clave se utilizan para salir de un bucle o continuar con la siguiente iteración, respectivamente. Por ejemplo:

```java
for (int i = 0; i < 10; i++) {
   if (i == 5) {
      break;
   }
   System.out.println("Iteración: " + i);
}
```

**return** : esta palabra clave se utiliza para salir de un método y devolver un valor (si es necesario). Por ejemplo:

```java
public int suma(int a, int b){
	return a + b;
}
```

**Array:** array en Java es una estructura de datos que permite almacenar un conjunto de valores del mismo tipo

```java
int[] miArray = new int[5];
miArray[0] = 1;
miArray[1] = 2;
miArray[2] = 3;

int[] miArray = {1, 2, 3, 4, 5};
```

# **La programación orientada a objetos (POO)**

es un paradigma de programación en el que los programas se dividen en objetos, que representan entidades del mundo real y contienen datos y comportamientos. Cada objeto es una instancia de una clase, que es una plantilla para crear objetos

## **clases**

las clases definen los atributos (o variables de instancia) y los comportamientos (o métodos) de los objetos. Una clase también puede contener constructores, que son métodos especiales que se usan para crear objetos de esa clase.

## **La Encapsulación**

Se refiere a la ocultación de los detalles de implementación de una clase detrás de una interfaz pública. Los atributos de una clase se declaran como privados y se accede a ellos a través de métodos públicos. Esto ayuda a proteger la integridad de los datos

## H**erencia**

Una clase puede heredar atributos y comportamientos de otra clase, lo que permite crear jerarquías de clases y ahorra tiempo y esfuerzo en la creación de nuevas clases

## P**olimorfismo**

Se refiere a la capacidad de un objeto para adoptar diferentes formas. En Java, esto se logra mediante la creación de clases que implementan una interfaz común o que heredan de una clase base.

```java
//Clase que representa un objeto de tipo Auto
public class Auto {
    //Atributos de la clase
    private String marca;
    private String modelo;
    private int año;
    private String color;
    
    //Métodos de la clase
    public void encender() {
        System.out.println("El auto se ha encendido");
    }
    
    public void acelerar() {
        System.out.println("El auto está acelerando");
    }
    
    public void frenar() {
        System.out.println("El auto está frenando");
    }
    
    public void apagar() {
        System.out.println("El auto se ha apagado");
    }
    
    //Getters y setters para los atributos
		//es un metodo que se utiliza para establecer el valor una propiedad de un obj
    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }
		// es un metodo que obtiene el valor de una propiedad de la clase
    public int getAño() {
        return año;
    }

    public void setAño(int año) {
        this.año = año;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
}

// Método estático (no necesita una instancia de la clase para ser llamado)
  public static int suma(int a, int b) {
    return a + b;
  }
  
  // Método final (no puede ser sobreescrito por una subclase)
  public final int resta(int a, int b) {
    return a - b;
  }
```

# Colecciones:

Las colecciones en Java son un conjunto de clases y interfaces que proporcionan una manera de almacenar y manipular conjuntos de objetos

ArrayList: Es una implementación de una lista que permite elementos duplicados y mantiene el orden de inserción.

```java
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> myList = new ArrayList<>();
        myList.add(1);
        myList.add(2);
        myList.add(3);
        myList.add(1);
        System.out.println(myList); // [1, 2, 3, 1]
    }
}
```

LinkedList: Es una implementación de una lista enlazada, permite elementos duplicados y mantiene el orden de inserción.

```java
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        LinkedList<String> myList = new LinkedList<>();
        myList.add("Hola");
        myList.add("mundo");
        myList.add("Hola");
        System.out.println(myList); // [Hola, mundo, Hola]
    }
}
```

HashSet: Es una implementación de un conjunto, no permite elementos duplicados y no mantiene el orden de inserción.

```java
import java.util.HashSet;

public class Main {
    public static void main(String[] args) {
        HashSet<Integer> mySet = new HashSet<>();
        mySet.add(1);
        mySet.add(2);
        mySet.add(3);
        mySet.add(1);
        System.out.println(mySet); // [1, 2, 3]
    }
}
```

TreeSet: Es una implementación de un conjunto ordenado, no permite elementos duplicados y mantiene el orden natural de los elementos o según un comparador especificado.

```java
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) {
        TreeSet<Integer> mySet = new TreeSet<>();
        mySet.add(3);
        mySet.add(2);
        mySet.add(1);
        mySet.add(1);
        System.out.println(mySet); // [1, 2, 3]
    }
}
```

HashMap: Es una implementación de un mapa, permite valores duplicados pero no claves.

```java
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        HashMap<String, Integer> myMap = new HashMap<>();
        myMap.put("uno", 1);
        myMap.put("dos", 2);
        myMap.put("tres", 3);
```

Manejo de Execepcion:

- es manejo de excepciones nos permite controlar,gestionar errores y excepciones que pueden ocurrir en nuestro codigo
- una excepcion es un evento que ocurre durante la ejecucion del programa que interumpe el flujo normal del programa
try{}catch(){}finally{}

throws: palabra clava se utiliza para especificar que el metodo va a lanzar una excepcion o varias excepciones
throw: se utiliza para lanzar una excepcion cuando se ejecuta una se interrumpe el flujo de norma de ejecucion del programa

JPA: java persistence api nos permite mapear clases de java a tablas de base datos esto nos permite trabaja don base de datos de manera sencilla utilizando
anotaciones de como se deben mapear
ORM(Object-Relational Mapping): es una tecnica de programacion que nos permite mapear objectos de un lenguaje de porgamacion a tablas de base de datos

ANNOTATIONS MAS USADAS:

Entity: especifica la creacion de una entidad se coloca al inicio de ladefinicion de una clase

id: primary key de la entidad
@GeneratedValue(strategy=GenerationType.AUTO): establece que la id se va generar de forma
automatica o secuencial
basic: atributos comunes
temporal: se usa en fechas
tener en cuenta la hora se utiliza: @temporal(temporal.type.timestamp)
tener en cuenta la fecha(date): @temporal(temporaltype.date)
@OneToMany: indica la relacion unidireccional de 1 a n
@OneToOne: indicar una relacion de 1 a 1
@ManyToMany: indicar una relacion n a n

JPA controllers : son clases que se encarga de operaciones crud en una base de datos utilizan la interfaz EntityManager
para realizar operaciones en la bd y mapear los obj de java a tablas de bd