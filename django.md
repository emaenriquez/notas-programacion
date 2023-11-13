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

views.py que vamos a querer a ejecutar
migrations
admin.py panel de administrador
apps.py configuracion de la app solo para una app
models.py para crear clases que se crean tablas sql
tests.py testing 

# Hello word

