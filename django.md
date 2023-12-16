# Entorno Virtual 

pip install virtualenv

virtualenv venv(entorno virtual)

Ctrl + shif p

selecionar inteprete: venv venv

# Instalar django

pip install django(instalar django)

django-admin --version

# Crear un projecto django
django-admin startproject mysite .

## crear un servidor en localhost

python manage.py runserver
python manage.oy runserver 3000

# Estructura de un proyecto
manage.py nos ayuda a ejecutar comandos administrativos

python manage.py --help

mysite el codigo funte de nuestra aplicacion
__int__.py nos indica que un modulo de python

settings.py este archivo es para configurar todo el projecto
https://docs.djangoproject.com/en/4.2/topics/settings/
urls sirve para manejar las url de nuestro projecto
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
db.sqlite3 base de datos 


# Creacion de una app

python manage.py startapp blog

## Estructura de las aplicacion

mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py



Estos archivos son:

El directorio raíz externo es un contenedor para el proyecto. Su El nombre no le importa a Django; Puedes cambiarle el nombre a lo que quieras.mysite/

manage.py: Una utilidad de la línea de comandos que le permite interactuar con este proyecto Django de diferentes formas

mysite/__init__.py: Un archivo vacío que le indica a Python que este directorio debería ser considerado como un paquete Python.

mysite/settings.py: Ajustes/configuración para este proyecto Django

mysite/urls.py: Las declaraciones URL para este proyecto Django; una «tabla de contenidos» de su sitio basado en Django.

mysite/asgi.py: Un punto de entrada para que los servidores web compatibles con ASGI Servir a su proyecto.

mysite/wsgi.py: Un punto de entrada para que los servidores web compatibles con WSGI puedan servir su proyecto.



# Include
sirve para incluir un bloque de urls de una aplicacion


```python

    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        # prefijo si pones home tenemos que poner en el localhost home/about 
        path('',include('myapp.urls'))
    ]
```

# Database modelos

En Django, los modelos de base de datos permiten definir la estructura de la base de datos de una aplicación. Estos modelos se utilizan para representar entidades y gestionar la interacción con la base de datos.

Migraciones
Las migraciones en Django son una forma de actualizar la base de datos desde Python. Pueden crear tablas y modificar el esquema de la base de datos. Para generar y aplicar migraciones, se utilizan los siguientes comandos:
```bash
python manage.py makemigrations
python manage.py migrate
```

Definición de Modelos
Los modelos se crean como clases de Python que heredan de django.db.models.Model. Cada atributo de la clase representa un campo en la tabla de la base de datos.

 ```python
from django.db import models

# Create your models here.

class Project(models.model):
    name = models.CharField(max_length=250)

class Task(models.Model):
    title = models.CharField(max_length=250),
    description = models.TextField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
 ```
Configuración en settings.py
Para que Django reconozca tus aplicaciones y modelos, asegúrate de agregar el nombre de tu aplicación al conjunto INSTALLED_APPS en el archivo settings.py. Por ejemplo:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp'
]
 ```

Generar y Aplicar Migraciones Específicas
Puedes generar y aplicar migraciones específicas para una aplicación con el siguiente comando:

```bash
python manage.py makemigrations myapp
python manage.py migrate myapp
```

# django shell

python manage.py shell

from myapp.models import Project, Task

p = Project(name="todo list")
p.save()

Project.objects.all()
```cmd
<QuerySet [<Project: Project object (1)>, <Project: Project object (2)
>]>
```
Project.pbjects.get(id=1)
Project.pbjects.get(id="todo list")

p = Project.pbjects.get(id=1)

p.task_set.all()

p.task_set.create()

Project.objects.filter(name_starswith="todo list")

<QuerySet [<Project: Project object (1)>]>

sino encuentra el nombre devuelve un query vacio

<QuerySet []>

p = Project.objects

p.filter(name_starswith="todo list")

# params
