

# GitHub Universe Cloud Skills Challenge


# Modulos

- [Introduccion a git](#Control-de-versiones-y-Git)
- [Procedimientos para crear y modificar un proyecto de Git](#Procedimientos-para-crear-y-modificar-un-proyecto-de-Git)
- [Colaboración con Git](#colaboración-con-git)
- [Edición de código mediante creación de ramas y combinación en Git](#edición-de-código-mediante-creación-de-ramas-y-combinación-en-git)
- [Introducción a GitHub](#introducción-a-github)
- [Código con GitHub Codespaces](#código-con-github-codespaces)
- [Introducción a GitHub Copilot](#introducción-a-github-copilot)
- [Uso de GitHub Copilot con JavaScript](#uso-de-github-copilot-con-javascript)
- [Uso de GitHub Copilot con Python](#uso-de-github-copilot-con-python)
- [Proyecto de desafío: Crear una aplicación de consola de minijuegos con GitHub Copilot](#proyecto-de-desafío-crear-una-aplicación-de-consola-de-minijuegos-con-github-copilot)
- [Proyecto de desafío: agregar funcionalidades de generación y análisis de imágenes a la aplicación](#proyecto-de-desafío-agregar-funcionalidades-de-generación-y-análisis-de-imágenes-a-la-aplicación)

### Control de versiones y Git

Un sistema de control de versiones (VCS) como Git permite rastrear cambios en archivos, recuperar versiones anteriores y colaborar en un proyecto sin interferir con el trabajo de otros. Git es un VCS de código abierto, rápido, versátil, escalable y gratuito.

#### Git y GitHub

Git es un sistema de control de versiones distribuido (DVCS) utilizado por desarrolladores y colaboradores para trabajar en un proyecto. GitHub es una plataforma en la nube que utiliza Git como tecnología principal, ofreciendo características como incidencias, debates, solicitudes de incorporación de cambios, notificaciones, etiquetas, acciones, bifurcaciones y proyectos.

#### Configuración y uso de Git

Para configurar Git, se utilizan los comandos `git config --global user.name "<USER_NAME>"` y `git config --global user.email "<USER_EMAIL>"`. Para iniciar un nuevo repositorio, se crea una carpeta para el proyecto (por ejemplo, `mkdir Cats`), se navega a ella (`cd Cats`) y se inicializa (`git init --initial-branch=main`).

Los comandos básicos de Git incluyen `git status` para ver el estado del árbol de trabajo, `git add` para almacenar provisionalmente los cambios, `git commit` para confirmar los cambios, `git log` para ver información sobre las confirmaciones anteriores y `git help` para obtener ayuda sobre los comandos de Git.

### Procedimientos para crear y modificar un proyecto de Git

#### Creación y adición de un archivo

Para crear un archivo y realizar la primera confirmación, se utilizan los siguientes comandos:
it status
git add .
git commit -m "Create an empty index.html file"


#### Recuperación de archivos

Si se elimina un archivo por accidente, se puede recuperar con `git checkout -- <file_name>`. Si se elimina un archivo con `git rm`, se puede recuperar con `git reset` y `git checkout`:
bash
git rm index.html
git reset HEAD index.html
git checkout -- index.html


#### Reversión de una confirmación
Si se comete un error en una confirmación, se puede revertir con `git revert`:
bash
git commit -m "Purposely overwrite the contents of index.html" index.html
git revert --no-edit HEAD

Estos comandos permiten revertir los cambios confirmados y volver a la versión anterior del archivo.

### Colaboración con Git

#### Clonación de un repositorio (git clone)
Se copia un repositorio con `git clone`, apuntando a una URL o ruta de acceso.

#### Repositorios remotos (git pull)
`git pull` copia cambios del repositorio remoto al local, insertándolos en el árbol de trabajo.

#### Solicitudes de incorporación de cambios (git request-pull)
`git request-pull -p origin/main .` permite revisar cambios de otros antes de incorporarlos al trabajo en el sitio web.

#### Creación de un remoto (git remote) y finalización de la solicitud de incorporación de cambios (git pull)
Se configura el repositorio de otro desarrollador como remoto con `git remote`, luego se usa ese remoto para incorporaciones y solicitudes de incorporación de cambios con `git pull`.

#### Clonación de un repositorio

```bash
cd ..
mkdir Alice
cd Alice
git clone ../Cats .
```

Ejercicio: Colaboración mediante un repositorio compartido

### Edición de código mediante creación de ramas y combinación en Git

#### Ramas en Git
El desarrollo de software se realiza casi por completo en ramas. El objetivo es mantener limpia la rama principal hasta que el trabajo esté listo . Después, inserte los cambios en la rama principal, o envíe una solicitud de incorporación de cambios para fusionar los cambios.

#### Estructura y nomenclatura de las ramas
Una rama es simplemente una cadena de confirmaciones que se ramifica a partir de la línea principal de desarrollo, como una rama de un árbol.

#### Creación y modificación de ramas (rama de Git y desprotección de Git)
Puede crear una rama con el comando git branch. Cambie entre las ramas con el comando git checkout.
checkout actualiza todo lo que hay en el árbol de trabajo y el índice para que coincida con la confirmación especificada (en este caso, el encabezado de la rama).

#### Combinación de ramas (combinación de Git)
Una vez que haya finalizado algún trabajo en una rama, quizá una característica o una corrección de errores, querrá combinar la rama de nuevo con la rama principal. Puede usar el comando git merge para combinar una rama específica con la rama actual.

```bash
# Switch back to the main branch
git checkout main

# Merge my-feature branch into main
git merge my-feature
```
hacer un modulo de git universe cloud skills challenge
hacer un ejercicio de exercism
hacer el ejercicio de codember

### Introducción a GitHub
### Código con GitHub Codespaces
### Código con GitHub Codespaces
### Uso de GitHub Copilot con JavaScript
### Uso de GitHub Copilot con Python
### Proyecto de desafío: Crear una aplicación de consola de minijuegos con GitHub Copilot
### Proyecto de desafío: agregar funcionalidades de generación y análisis de imágenes a la aplicación