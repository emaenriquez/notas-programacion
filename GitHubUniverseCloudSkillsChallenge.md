

# GitHub Universe Cloud Skills Challenge


# Modulos

## Introduccion a git

### ¿Qué es el control de versiones?

Un sistema de control de versiones (VCS) es un programa o conjunto de programas que realiza un seguimiento de los cambios en una colección de archivos
- objectivos:
	- Recuperar fácilmente versiones anteriores de archivos individuales o de todo el proyecto
	- permitir que varios miembros de un equipo trabajen en un proyecto, incluso en los mismos archivos, al mismo tiempo sin que eso afecte al trabajo de los demás.
Git es un VCS de código abierto rápido, versátil, muy escalable y gratuito

### Control de versiones distribuido
Git es un sistema distribuido, lo que significa que el historial completo de un proyecto se almacena en el cliente y en el servidor.
editar archivos sin conexión de red, protegerlos localmente y sincronizarlos con el servidor cuando una conexión esté disponible.
si un servidor deja de funcionar, todavía tendrá una copia local del proyecto.

### Terminología de Git

- Árbol de trabajo: conjunto de directorios y archivos anidados que contienen el proyecto en el que se trabaja.

- Árbol de trabajo: conjunto de directorios y archivos anidados que contienen el proyecto en el que se trabaja.

- Hash: número generado por una función hash que representa el contenido de un archivo u otro objeto como un número de dígitos fijo  Una ventaja de usar códigos hash es que Git puede indicar si un archivo ha cambiado aplicando un algoritmo hash a su contenido y comparando el resultado con el hash anterior. Si se cambia la marca de fecha y hora del archivo, pero el hash del archivo no, Git sabe que el contenido del archivo no se ha modificado.

- Objeto: un repositorio de Git contiene cuatro tipos de objetos, cada uno identificado de forma única por un hash SHA-1. 
	- Un objeto blob contiene un archivo normal. 
	- Un objeto árbol representa un directorio, y contiene nombres, valores hash y permisos. 
	- Un objeto de confirmación representa una versión específica del árbol de trabajo. Una etiqueta es un nombre asociado a una confirmación.

- Confirmación: Significa que se confirman los cambios realizados para que otros usuarios también puedan verlos.

- Rama: serie con nombre de confirmaciones vinculadas. La confirmación más reciente en una rama se denomina nivel superior. La rama predeterminada, que se crea al inicializar un repositorio, se denomina main, y suele tener el nombre master en Git. El nivel superior de la rama actual se denomina HEAD. Las ramas son una característica increíblemente útil de Git porque permiten a los desarrolladores trabajar de forma independiente (o conjunta) en ramas y luego combinar los cambios en la rama predeterminada.

- Remoto: referencia con nombre a otro repositorio de Git. Cuando se crea un repositorio, Git crea un remoto denominado origin, que es el remoto predeterminado para las operaciones de envío e incorporación de cambios.

- Comandos, subcomandos y opciones: las operaciones de Git se realizan mediante comandos como git push y git pull. git es el comando, mientras que push o pull es el subcomando. El subcomando especifica la operación que quiere que Git realice. Los comandos suelen ir acompañados de opciones, que usan guiones (-) o guiones dobles (--). Por ejemplo, git reset --hard.

### Git y GitHub
-  Git es un sistema de control de versiones distribuido (DVCS) que varios desarrolladores y otros colaboradores pueden usar para trabajar en un proyecto
- GitHub es una plataforma en la nube que usa Git como tecnología principal

Entre las características clave que ofrece GitHub se incluyen las siguientes:
- Incidencias
- Debates
- Solicitudes de incorporación de cambios
- Notificaciones
- Etiquetas
- Acciones
- Bifurcaciones
- Proyectos

### Configuración de Git

git --version
git config --global user.name "<USER_NAME>"
git config --global user.email "<USER_EMAIL>"
git config --list

user.name=User Name
user.email=user-name@contoso.com

### Configuración del repositorio de Git

Git funciona buscando cambios en los archivos dentro de una determinada carpeta. Vamos a crear una carpeta que actúe como árbol de trabajo (directorio del proyecto) y a permitir que Git sepa sobre ella para que pueda comenzar a seguir los cambios

Cree una carpeta con el nombre Cats. Esta carpeta va a ser el directorio del proyecto, también denominado árbol de trabajo. 

mkdir Cats

Vaya al directorio del proyecto mediante el comando
cd Cats

Ahora, inicialice el nuevo repositorio y establezca el nombre de la rama predeterminada en main:

git init --initial-branch=main
git init -b main

git init
git checkout -b main

Después de ejecutar el comando de inicialización, debería ver una salida similar a la de este ejemplo:
Initialized empty Git repository in /home/<user>/Cats/.git/

Switched to a new branch 'main'

Ahora, use un comando git status para mostrar el estado del árbol de trabajo:
git status

Git responde con esta salida, que indica que master es la rama actual. (De hecho, también es la única rama). Por ahora todo está claro.

On branch master

 No commits yet

 nothing to commit (create/copy files and use "git add" to track)

Use un comando ls para mostrar el estado del árbol de trabajo:
ls -a


### Ayuda desde Git
git --help

### Comandos básicos de Git

- git status
	- muestra el estado del árbol de trabajo Permite ver los cambios que Git está siguiendo en ese momento para poder decidir si quiere pedir a Git que tome otra instantánea.
- git add
	- Va a usar git add para almacenar provisionalmente los cambios a fin de prepararse para una confirmación. 
	- Va a usar git add para almacenar provisionalmente los cambios a fin de prepararse para una confirmación. 
- git commit
	-  una confirmación es el pequeño fragmento de datos que asigna una identidad única a los cambios que se confirman. Los datos que se guardan en una confirmación incluyen el nombre del autor y la dirección de correo electrónico, la fecha, los comentarios sobre lo que se ha hecho (y por qué)
- git log 
	- El comando git log permite ver información sobre las confirmaciones anteriores. Cada confirmación tiene un mensaje adjunto , y el comando git log permite imprimir información sobre las confirmaciones más recientes, como su marca de tiempo, el autor y un mensaje de confirmación
- git help
	- Por ejemplo, git commit --help muestra una página que proporciona más información sobre el comando git commit y cómo usarlo


## Procedimientos para crear y modificar un proyecto de Git


### Ejercicio: Inicio de un proyecto

Creación y adición (almacenamiento provisional) de un archivo

Use un comando touch para crear un archivo denominado index.html:

touch index.html
git status
git add .

Realización de la primera confirmación

Utilice el comando siguiente para crear otra confirmación:
git commit index.html -m "Create an empty index.html file"

Git solo realiza el seguimiento de los cambios en los archivos, no en los directorios.