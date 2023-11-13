

# GitHub Universe Cloud Skills Challenge


# Modulos

- [Introduccion a git](#Control-de-versiones-y-Git)
- [Procedimientos para crear y modificar un proyecto de Git](#Procedimientos-para-crear-y-modificar-un-proyecto-de-Git)
- [Colaboración con Git](#colaboración-con-git)
- [Edición de código mediante creación de ramas y combinación en Git](#edición-de-código-mediante-creación-de-ramas-y-combinación-en-git)
- [Introducción a GitHub](#introducción-a-github)
- [Código con GitHub Codespaces](#código-con-github-codespaces)
- [Introducción a GitHub Copilot](#Introducción-a-GitHub-Copilot)
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


### Introducción a GitHub

#### ¿Qué es GitHub?

Aquí se describen las principales características de GitHub que se usan a diario para administrar y contribuir a proyectos de software.

#### El flujo de GitHub

Además de ser una plataforma de desarrollo de software colaborativo, GitHub ofrece también un flujo de trabajo diseñado para optimizar el uso de sus diversas características

#### Git y GitHub

Git es un sistema de control de versiones distribuido (DVCS) que permite que varios desarrolladores u otros colaboradores trabajen en un proyecto.

GitHub es una plataforma en la nube que usa Git como tecnología principal. Simplifica el proceso de colaborar en proyectos y proporciona un sitio web, herramientas de línea de comandos y un flujo global que permite a los desarrolladores y usuarios trabajar juntos.

#### Las características principales de GitHub incluyen:

- Issues
- Debates
- Solicitudes de incorporación de cambios
- Notificaciones
- Etiquetas
- Acciones
- Horquillas
- Proyectos

#### Incidencias

Las incidencias son el elemento en el que se produce la mayor parte de la comunicación entre los consumidores y el equipo de desarrollo de un proyecto. Puede crear una incidencia para analizar una amplia variedad de temas, como informes de errores, solicitudes de características, aclaraciones sobre la documentación, etc. Una vez creado un problema, puede asignar propietarios, etiquetas, proyectos e hitos. Las incidencias también se pueden asociar con solicitudes de incorporación de cambios y otros elementos de GitHub para proporcionar rastreabilidad en el futuro.

#### Notificaciones
Como plataforma colaborativa, GitHub ofrece notificaciones para prácticamente todos los eventos que se producen en un flujo de trabajo determinado.

#### Ramas
Las ramas son la manera preferida de crear cambios en el flujo de GitHub. Proporcionan aislamiento para que varias personas puedan trabajar simultáneamente en el mismo código de manera controlada.

#### Confirmaciones
Un commit refleja uno o varios cambios en uno o varios archivos de una rama. Cada vez que se crea una confirmación, se le asigna un identificador único y se realiza un seguimiento de ella, junto con la hora y el colaborador.

#### Solicitudes de incorporación de cambios
Una solicitud de incorporación de cambios es un mecanismo que sirve para indicar que las confirmaciones de una rama están listas para combinarse en otra. El desarrollador que envíe la solicitud de incorporación de cambios normalmente solicitará a uno o varios revisores que comprueben el código y aprueben la combinación

#### Etiquetas
Las etiquetas proporcionan una manera de categorizar y organizar las incidencias y las solicitudes de incorporación de cambios en un repositorio

#### Acciones
Las acciones de GitHub proporcionan funcionalidad de flujo de trabajo y automatización de tareas en un repositorio. Puede usar las acciones para simplificar los procesos del ciclo de vida de desarrollo de software e implementar la integración y la implementación continuas (CI/CD).

#### Clonación y bifurcación

- Clonar un repositorio: al clonar un repositorio, se realiza una copia del repositorio y de su historial en el equipo local. 

- Bifurcación de un repositorio: al bifurcar un repositorio, se realiza una copia del repositorio en la cuenta de GitHub. El repositorio principal se denomina ascendente, mientras que la copia bifurcada se conoce como origen. Una vez que haya bifurcado un repositorio en la cuenta de GitHub, puede clonarlo en el equipo local. 


¿Cuándo debería clonar un repositorio en lugar de bifurcarlo? Si está trabajando con un repositorio y tiene acceso de escritura, puede clonarlo en el equipo local. Desde allí, puede realizar modificaciones e introducir los cambios directamente en el repositorio de origen.

Si necesita trabajar con un repositorio creado por otro propietario, como github/example, y no tiene acceso de escritura, puede bifurcar el repositorio en su cuenta de GitHub y, luego, clonar la bifurcación en el equipo local. 


### Código con GitHub Codespaces

#### GitHub Codespaces 
es un entorno de desarrollo instantáneo basado en la nube que usa un contenedor para proporcionar lenguajes, herramientas y utilidades comunes para el desarrollo.

#### Ciclo de vida de un codespace
GitHub Codespaces se puede configurar, lo que le permite crear un entorno de desarrollo personalizado para el proyecto.

Al configurar un entorno personalizado para el proyecto y 
puedo tener una configuración de codespace repetible para todos los usuarios del proyecto.

#### Crear un codespace
Puede crear un codespace en GitHub.com, en Visual Studio Code o en la CLI de GitHub. Existen cuatro formas de crear un codespace:

- Desde una plantilla de GitHub o desde cualquier repositorio de plantillas de
GitHub.com para iniciar un nuevo proyecto
- Desde una rama del repositorio para el trabajo de nuevas características.
- Desde una solicitud de cambios abierta para explorar el trabajo en curso
- Desde una confirmación en el historial de un repositorio para investigar un error en
un punto específico del tiempo.

Puede usar un codespace temporalmente para probar código o volver al mismo codespace para realizar trabajo de características de larga duración.

Puede crear más de un codespace por repositorio o incluso por rama. Sin embargo, hay límites respecto al número de codespaces que puede crear y ejecutar al mismo tiempo. Si alcanza el número máximo de codespaces e intenta crear otro, aparece un mensaje que indica que se debe quitar o eliminar un codespace existente para poder crear uno nuevo.

Puede crear un nuevo codespace cada vez que desarrolle en GitHub Codespaces o mantener un codespace de larga duración para una característica. Si va a iniciar un proyecto nuevo, cree un codespace a partir de una plantilla y publíquelo en un repositorio de GitHub más adelante.

Al crear un codespace cada vez que se trabaja en un proyecto, debe enviar los cambios periódicamente para asegurarse de que todas las confirmaciones nuevas estén en GitHub. Al usar un codespace de larga duración para un proyecto nuevo, incorpore los cambios desde la rama predeterminada del repositorio cada vez que empiece a trabajar en el codespace. Esto permite al entorno obtener las últimas confirmaciones. El flujo de trabajo es similar a trabajar con un proyecto en una máquina local.

Los administradores de repositorios pueden habilitar las precompilaciones de GitHub Codespaces para que un repositorio acelere la creación de un codespace.

Para ver un tutorial y una guía detallados, consulte los recursos Guía para principiantes para aprender a codificar con GitHub Codespaces y Desarrollar en un codespace que se encuentran en la unidad Resumen al final de este módulo.


#### Al crear un codespace tienen cuatro procesos:

- Se asignan al codespace una máquina virtual y almacenamiento.
- Se crea un contenedor.
- Se establece una conexión con el codespace.
- Se realiza una configuración posterior a la creación.

#### Guardar cambios en un codespace
Cuando se conecta a un codespace a través de la web, se habilita de forma automática la opción de autoguardado para guardar los cambios cuando haya transcurrido una cantidad de tiempo específica

#### Apertura de un codespace existente
Para reanudar un codespace existente, puede ir al repositorio donde existe el codespace, presionar la tecla "," en el teclado y seleccionar Reanudar este codespace

#### Tiempos de espera de un codespace
Si un codespace está inactivo o si sale del codespace sin detenerlo de forma explícita, la aplicación agota el tiempo de espera después de un período de inactividad y deja de ejecutarse.

#### Cerrar o detener un codespace
Si sale del codespace sin ejecutar el comando para detenerlo (por ejemplo, cierra la pestaña del explorador) o si deja el codespace en ejecución sin interacción, el codespace y sus procesos en ejecución continuarán durante el período de tiempo de espera de inactividad

#### Recompilación de un codespace
Puede recompilar el codespace para implementar cambios en la configuración de contenedor de desarrollo. Para la mayoría de los usos, puede crear un codespace como alternativa a recompilar uno

#### Eliminar un codespace
Puede crear un codespace para una tarea determinada. Después de enviar los cambios a una rama remota, puede eliminar ese codespace de forma segura.

### Introducción a GitHub Copilot

#### Introducción
GitHub Copilot es la primera herramienta para desarrolladores de inteligencia artificial a escala del mundo que puede ayudarle a escribir código más rápidamente y con menos trabajo

### Uso de GitHub Copilot con JavaScript
### Uso de GitHub Copilot con Python
### Proyecto de desafío: Crear una aplicación de consola de minijuegos con GitHub Copilot
### Proyecto de desafío: agregar funcionalidades de generación y análisis de imágenes a la aplicación