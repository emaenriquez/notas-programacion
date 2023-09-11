# Variables

## Variables

```dart
// Si un objeto no está restringido a un solo tipo, Especifique el tipo 
// (o, si es necesario)
Object name = 'emanuek';
// declarar explícitamente el tipo
String name_str = 'la conda';
```

## Seguridad Nula

se le asigna el valor nulo a la variable
deja que valor sea nulo ya que dart no acepta valores nulos y te obliga a establecer un valor inicial

```dart
String? numero; // va a salir que es nulo
String numero_2; // va a saltar un error
```

```dart
int? lineCount;

if (lineCount == 10) {
    print('es 10');
} else {
    print('no es 10');
}
```

## Variables Tardarías

```dart
late String description;

void main() {
  description = 'Feijoada!';
  print(description);
}
```

## **Final**

una variable final no puede cambiarse

```dart
final name = 'bob';
name = 'Alice'; // Error: a final variable can only be set once.
final String m = 'bobby';
```

## Cosnt
```dart
var food = const[];
final baz = const[];
const faz = [];
  
food = [1,2,3,4];
baz = [1,2,3,4,5];
  
print(food);
print(baz);

const Object i = 3;
const list = [ i as int];
const map = {if( i is int) i: 'int'};
const set = {if(list is List<int>) ...list};
print(i);
```

# Operadores

## Operadores aritméticos
```dart
print(2 + 3 == 5);
print(2 - 3 == -1);
print(2 * 3 == 6);
print(5 / 2 == 2.5); // Result is a double
print(5 ~/ 2 == 2); // Result is an int
print(5 % 2 == 1); // Remainder
```

## Igualdad y operadores relacionales
```dart
assert(2 == 2);
assert(2 != 3);
assert(3 > 2);
assert(2 < 3);
assert(3 >= 3);
assert(2 <= 3);
```
## **Operadores de prueba de tipo**

1. Utilizamos el operador **`as`** para intentar convertir un valor dinámico (**`dynamicValue`**) a un tipo específico (**`String`**). Si la conversión tiene éxito, el valor convertido se asigna a la variable **`stringValue`**.
2. Utilizamos el operador **`is`** para comprobar si una variable (**`number`**) tiene el tipo **`int`**.
3. Utilizamos el operador **`is!`** para verificar si una variable (**`value`**) no tiene el tipo **`int`**.
```dart
void main() {
  // Ejemplo con el operador "as"
  dynamic dynamicValue = "Hola";
  String stringValue = dynamicValue as String; 
	// Intentamos convertir dynamicValue a String
  print("Valor convertido: $stringValue");
```
```dart
void main() {
  // Ejemplo con el operador "is!"
  var value = 3.14;
  if (value is! int) {
    print("El valor no es un entero.");
  } else {
    print("El valor es un entero.");
  }
}
```
```dart
void main() {

  // Ejemplo con el operador "is"
  var number = 42;
  if (number is int) {
    print("El número es un entero.");
  } else {
    print("El número no es un entero.");
  }
}
```