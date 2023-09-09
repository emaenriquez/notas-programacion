
# notas c

## hola mundo
```c
    #include <stdio.h>

    int main(){

        printf("Hola mundo\n");

        return 0;
    }
```

## sumar dos numeros

#include <stdio.h>
```c
int main(){
    int num1;
    int num2;
    int res;

    printf("ingrese el numuero1\n");
    scanf("%d",&num1);

    printf("ingrese el numero2\n");
    scanf("%d",&num2);

    res = num1 + num2;

    printf("el resultado es: %d\n",res);
    
    return 0;

}

```
## condicionales 
```c
    #include <stdio.h>

    int main(){
    // == !=
    // < > <= >=
    int edad;
    printf("ingresa tu edad");
    scanf("%d",&edad);

    if(edad >= 18){
        printf("eres mayor de edad");
    } else if(edad >= 17){
        printf("casi eres mayor de edad");
    } 
    else{
        printf("eres menor de edad");
    }
}
```
## directivas
```c
    /* Directivas del pre-procesador*/
    #include <stdio.h> // va a buscar en la biblioteca estandar
    // #include "nombre del archivo " // va a buscar en la misma carpeta
    #define PI 3.14 // crear constate simbolicas y macros
    #define CUBO(a) a*a*a

    int main(){ 
    // int suma;
    // suma = PI + 3;

    // printf("la suma es: %d\n",suma);

    int a = 3;
    printf("el cubo de la variable a: %d\n",CUBO(a));

    return 0;
}
```
## variables
```c
    #include <stdio.h>

    int main(){
    
        char letra = 'a'; // tamaño 1 byte 0...255
        printf("%c\n",letra);

        int numero = 20; // 2 byte -32768 ... 32767
        printf("%i\n",numero);

        short sho = -1; // 2 bytes -128...127
        printf("%i\n",sho);

        unsigned int numero_unsigned =25; // 2 bytes 0...65535
        printf("%i\n",numero_unsigned);

        long numero_long = 5523; //4 bytes -2147483648...2147483647
        printf("%li\n",numero_long);

        float numero_float = 5.2212; // 4 bytes
        printf("%.2f\n",numero_float);

        double numero_double = 5212.2212; // 8 bytes 
        printf("%.lf\n",numero_double);

}
```
## convert
```c
   #include <stdio.h>
    /*palabras reservadas y conversion de tipos de datos*/
    int main(int argc, char const *argv[])
    {
        // int a = 23;
        // int a = 80; es la P en codigo aski
        int a = 80;
        float f = 23.321;
        float suma = (float)a + f;
        printf("la suma es: %f\n",suma);
        printf("entero%i\n flotante%.2f\n double%.3f\n caracter%c\n",a,(float)a,(double)a,(char)a);
        return 0;
    }
```
## ciclo For
```c
   #include <stdio.h>

    int main(int argc, char const *argv[])
    {
        int count = 10;
        for (int i = 0; i <= count; i++)
    {
        printf("numeros del ciclo:%i\n",i);
    }

    return 0;
}

```
## while
```c
    #include <stdio.h>

    int main(int argc, char const *argv[])
    {
        int contador = 0;

        while (contador <= 10)
        {
            printf("numeros del ciclo: %i\n",contador);
            contador++;
        }
    
        return 0;
    }
```
## dowhile
```c
    #include <stdio.h>

    int main(int argc, char const *argv[])
    {
        int contador = 1;
        do
        {
            printf("%i\n",contador);
            contador++;
        } while (contador <=10);

        return 0;
    }
```
## break continue
```c
    #include <stdio.h>

    int main(int argc, char const *argv[])
    {
        int num = 0;
        while (num <= 7)
        {
        num++;
        // if( num == 2) break;
        if(num == 2) continue;
        printf("el valor del numer: %i\n",num);
    }
    
    return 0;
    }
```
## directivas
```c
    #include <stdio.h>

    int main(int argc, char const *argv[])
    {
        int caso;
        printf("ingrese un numero\n");
        scanf("%i",&caso);
        switch (caso)
        {
        case 1:
            printf("el numero ingresado es: 1");
            break;
        case 2:
            printf("el numero ingresado es: 2");
            break;
        case 3:
            printf("el numero ingresado es: 3");
            break;
        default:
        printf("el numero ingresado no esta en ninguno de los casos");
            break;
        }    

        return 0;
    }

```
## Array
```c
    #include <stdio.h>

    int main(int argc, char const *argv[])
    {

        // int arr_enteros[10] = {0,1,2,3,4,5,6,7,8,9};
        // printf("%i\n",arr_enteros[0]);

        int tamano;

        printf("tamaño del arreglo\n");
        scanf("%i",&tamano);

        int edades[tamano];

        for (int i = 0; i < tamano; i++)
        {
            printf("ingresa el valor %i\n",i+1);
            scanf("%i",&edades[i]);
        }

        printf("los valores del arreglo son: \n");

        for (int i = 0; i < tamano; i++)
        {
            printf("los valores son %i\n",edades[i]);
        }


        return 0;   
    }   

```
## funciones
```c
    #include <stdio.h>

    printf("hola humdo funicona z   AA");
    void saludo(){
        return;
    }
    int suma();

    int main(int argc, char const *argv[])
    {
        /* code */
        saludo();
        printf("%i\n",suma());
        return 0;
    }

    int suma(){
        int num1 = 10;
        int num2 = 10;
        int res = num1 + num2;

        return res;
    }
```
## funciones sin retorno
```c
    #include <stdio.h>

    int main(int argc, char const *argv[])
    int suma();    
    {                        
        int num1;
        int num2;

        printf("ingresa el primer valor");
        scanf("%i",&num1);
        printf("ingresa el segundo valor");
        scanf("%i\n",&num2);

        printf("el resultado es: %i\n",suma(num1,num2));
        return 0;
    }

    int suma(int num1,int num2){

        int suma = num1 + num2;
        return suma;
    }
```
## funciones recursivas
```c
    #include <stdio.h>

    long Factorial(long numero);
    int main(int argc, char const *argv[])
    {
 
        int numero;

        printf("ingrese un numero \n");
        scanf("%i",&numero);

        for (int i = 0; i <= numero; i++)
        {

            printf("%ld\n",Factorial(i));

        }

        return 0;
    }

    long Factorial(long numero)
    {
        if(numero <= 1)
        {
            return 1;
        } else
        {
            return(numero * Factorial(numero-1));
        }
    }
    
```
## apuntadores
```c
    
    #include <stdio.h>

    /*
        apuntadores en C
        son variables cuyo valores son direcciones de memoria
        un apuntador contiene la direccion de una variable que contiene un valor espeficico
    */
    int main(int argc, char const *argv[])
    {
        int a = 2;
        int *apt = &a;

        // printf("%i",*apt);
        printf("%p\n",apt); // muestra en espacio en memoria tipo exadecimal

        return 0;
    }

```
## apuntadores con referencia
```c
    #include <stdio.h>

    /* apuntadores pasados por referencia */

    /*llamada por valor*/
    // int cubo(int n);
    // int main(int argc, char const *argv[])
    // {
    //     int num = 5;
    //     printf("pasar el valor al cubo %i\n", num);

    //     num = cubo(num);

    //     printf("el nuevo valor %i\n", num);

    //     return 0;
    // }

    // int cubo(int n)
    // {
    //     return n * n * n;
    // }

    // llamada por referencia 
    void cubo(int *n);
    int main(int argc, char const *argv[])
    {
        int num = 5;
        printf("pasar el valor al cubo %i\n", num);

        cubo(&num);

        printf("el nuevo valor %i\n", num);

        return 0;
    }

    void cubo(int *n)
    {
        *n = *n * *n * *n;
    }
```
## Size Of
```c
    #include <stdio.h>

    size_t getsize(float *ptr);
    /* oprerador size of determina el tamaño en bytes de un arreglo*/
    int main(int argc, char const *argv[])
    {
        float arr[20];

        printf("El numero en bytes de un arreglo es: %lu\n",sizeof(arr));
        printf("El numero en bytes devueltos de getsieze es:  %lu\n",getsize(arr));

        return 0;
    }

    size_t getsize(float *ptr)
    {
        return sizeof(ptr);
    }
```
## Estructura
```c
    
    #include <stdio.h>
    struct perro
    {
        char nombre[30];
        int edad;
        float peso;
    }
    perro1 ={"Toni",5,16.2},
    perro2 ={"ternera",3,10.00};



    /*una estructura es una collecion de uno o mas tipos de elementos*/
    int main(int argc, char const *argv[])
    {
        printf("el peso es: %s es %.2f y tiene %i meses \n",perro1.nombre,perro1.peso,perro1.edad);
        return 0;
    }

```
## Array Estructura
```c
    #include <stdio.h>
    struct perro
    {
        char nombre[30];
        int edad;
        float peso;
    }
    perro1[3];
    int main(int argc, char const *argv[])
    {
        for (int i = 0; i < 3; ++i)
        {
            printf("%i ingresa el nombre del perro",i+1);
            scanf("%s\n",&perro1[i].nombre);
            // printf("%i ingresa la edad del perro",i+1);
            // scanf("%i\n",&perro1[i].edad);
            // printf("%i ingresa el peso del perro",i+1);
            // scanf("%.2f\n",&perro1[i].peso);
        }

        for (int i = 0; i < 3;++i)
        {
            printf("%i El nombre de los perros son: %s\n",i+1,perro1[i].nombre);
            // printf("%i La edad de los perros son: %s\n",i+1,perro1[i].edad);
            // printf("%i El peso de los perros son: %s\n",i+1,perro1[i].peso);
        }
        
        return 0;
    }
```