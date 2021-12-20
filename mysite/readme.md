### DJANGO - Aplicación base para una implementación de producción adecuada y segura
---
#### Introducción
En este tutorial, procederemos a explicar paso a paso en una máquina Kali Linux o Ubuntu, a como realizar una máquina virtual que contenga una aplicación base de Django con una implementación adecuada y segura, en el cual seguiremos unas previas características y arquitectura de producción para conseguir lograrlo.

#### Características
Las características que seguiremos para lograr la adecuada implementación de nuestra aplicación Django serán las siguientes:
- Configurar un virtualenv con las librerías adecuadas (requirements.txt).
- Crear el proyecto con las versiones adecuadas y actualizadas.
- Tener el proyecto bajo un VCS (sistema de versionado) como Git.
- Configurar los datos sensibles del proyecto (contraseñas, tokens, etc.) porque no se publiquen al repositorio de código.
- Habilitar configuración de la app mediante variables de entorno, en ninguna parte de ficheros.
- Hacer un README para facilitar la clonación y posta en marcha del proyecto.
- Configurar la BD adecuadamente.
- Configurar el servidor de archivos estáticos.
- Poner el proyecto en producción con un servidor de aplicaciones (uWSGI) + un servidor web (Nginx) para los archivos estáticos.

#### Arquitectura
![Arquitectura App DJANGO](https://bytes.cat/_media/diagrama_django_produccio.png)

#### Instalación de las herramientas necesarias para la creación de nuestra máquina virtual 
Sabiendo ya el objetivo que tenemos en mente, pasaremos a realizar la máquina virtual la cual contendrá nuestra aplicación de Django. En este caso, utilizaremos la herramienta Vagrant, herramienta que utilizaremos para crear nuestra máquina virtual en el software de virtualización Virtualbox de una manera mucho más rápida, dado que, evitaremos hacer la instalación del sistema operativo.
Dicho esto, procederemos a instalar las herramientas necesarias para efectuar esta acción, en este caso, la herramienta Vagrant y el software de virtualización Virtualbox. Para ello, deberemos abrir nuestra consola (*Control + Alt + T*) y ejecutar los siguientes comandos:
```
1. sudo apt update
2. sudo apt upgrade -y
3. sudo apt install vagrant -y 
4. sudo apt install virtualbox -y
```

#### Creación de nuestra máquina virtual
Una vez hayamos finalizado la instalación de las herramientas necesarias para la creación de nuestra máquina virtual, procederemos a ello, es decir, pasaremos a crear la máquina virtual con la que trabajaremos a partir de este punto.
Dicho esto, crearemos una máquina virtual con el sistema operativo *Ubuntu Focal Fossa* la cual cubrirá todas las necesidades necesarias para la realización de nuestra aplicación Django. Hecho este inciso, procederemos a crear nuestra máquina virtual dentro de un directorio en el cual se quedará guardada ejecutando los siguientes comandos en nuestra consola:
```
1. mkdir nombre_que_deseas_asignarle_a_tu_directorio
2. cd nombre_que_le_hayas_asignado_a_tu_directorio
3. sudo vagrant init ubuntu/focal64
```
#### Edición del archivo Vagrantfile para tener acceso a la red externa en nuestra máquina virtual
Cuando hayamos finalizado la creación de nuestra máquina virtual Ubuntu Focal Fossa, tendremos que modificar el archivo Vagrantfile, archivo que automáticamente la herramienta Vagrant generará cuando originemos una máquina virtual, ya que, es el archivo de configuración de dicha máquina. En dicho archivo, tendremos que descomentar una línea la cual nos permitirá tener acceso a la red externa, es decir, tener acceso a Internet. Por dicha razón, seguiremos los pasos siguientes:
```
1. sudo nano Vagrantfile
```
Seguidamente, cuando nos encontremos en el archivo Vagrantfile, descomentaremos la siguiente línea:
```
config.vm.network "public_network"
```
Y guardaremos los cambios con la combinación de teclas Control + O y saldremos del archivo con Control + X.

#### Acceso a nuestra máquina virtual Ubuntu Focal Fossa
Justo después de que hayamos realizado todo lo indicado en el punto anterior, ya estaremos preparados para poder acceder sin problemas a la máquina virtual que hemos creado con la herramienta Vagrant. Para ello, solamente deberemos ejecutar los siguientes comandos mostrados a continuación:

*(En el primer comando que ejecutemos, posiblemente nos soliciten seleccionar una de nuestras tarjetas de red que tengamos en nuestra máquina física, en ese caso, solamente deberemos indicar aquella tarjeta de red a utilizar con el número que nos indiquen)*
```
1. sudo vagrant up
2. sudo vagrant ssh
```
#### Instalación de Byobu en nuestra máquina virtual Ubuntu Focal Fossa
Una vez hayamos accedido a nuestra máquina virtual Ubuntu Focal Fossa, pasaremos a instalar la herramienta Byobu, herramienta que nos permitirá dividir una consola en múltiples secciones o generar sesiones independientes en la misma terminal y que nos podrá servir de gran ayuda para realizar más tareas al mismo tiempo.
Explicado esto, para la instalación de dicha herramienta deberemos ejecutar los siguientes comandos en nuestra máquina virtual:
```
1. sudo apt update
2. sudo apt upgrade -y
3. sudo apt install byobu -y
4. byobu-enable
```
Posteriormente, deberemos salir de nuestra máquina virtual y volver a acceder para que se apliquen los cambios de dicha herramienta. Para ello, ejecutaremos los siguientes comandos:

*(Este primer comando lo ejecutaremos en nuestra máquina virtual)*
```
1. exit
```
*(Y este segundo, lo ejecutaremos en la consola de nuestra máquina física. Recalcar que, deberemos encontrarnos en el directorio que creamos para guardar nuestra máquina virtual.)*
```
2. sudo vagrant ssh
```

#### Creación de nuestro entorno Python Venv y proyecto Django
Después de que hayamos finalizado la instalación de la herramienta Byobu, pasaremos a la realización de un entorno Python que nos servirá para aislar las diferentes versiones de librerías que usemos de nuestra máquina virtual, consiguiendo así, evitar posibles incompatibilidades. Dicho esto, pasemos a ejecutar todos los comandos necesarios para poder lograr la creación de este entorno:
```
1. sudo apt install python3.8-venv -y
2. python3 -m venv nombre_que_le_quieres_asignar_a_tu_entorno_virtual
3. ls
```
Una vez llegados a este punto, veremos que se nos habrá creado sin problemas nuestro entorno virtual Python, el cuál accederemos en todo momento para realizar las tareas de aquí hacía adelante para evitar posibles problemas. Por dicha razón, para acceder a dicho entorno, deberemos ejecutar el siguiente comando:
```
1. source nombre_de_tu_entorno_virtual/bin/activate
```
Ulteriormente, veremos que nos habrá accedido a nuestro entorno virtual exitosamente, dado que, en el lado izquierdo de nuestra consola nos aparecerá entre paréntesis el nombre del entorno virtual que creamos, viendo una cosa así:
```
(nombre_de_nuestro_entorno_virtual) vagrant@ubuntu-focal:~$
```
Siendo esto así, podremos continuar sin problemas. En este caso, pasaremos a realizar nuestro proyecto Django y posteriormente a arrancarlo para visualizar si todo funciona correctamente.
Comentado esto, veamos los comandos que deberemos ejecutar para lograr la creación de nuestro proyecto Django:

*(En el cuarto comando que ejecutemos, deberemos recordar nuestra dirección IP, dado que, lo necesitaremos para poder acceder posteriormente a nuestro proyecto Django a través de un navegador web)*
```
1. pip install django
2. django-admin startproject mysite
3. cd mysite
4. ip addr | grep inet
5. python3 manage.py runserver 0.0.0.0:8000
```
Seguidamente, cuando hayamos arrancado nuestro proyecto Django, nos dirigiremos a nuestro navegador web y en la barra de búsqueda situada en la parte superior, escribiremos la dirección IP de nuestra máquina virtual con el puerto 8000, es decir, lo siguiente con tu respectiva dirección IP:
```
tu_dirección_IP:8000
```
Enseguida, veremos que se nos cargará sin problemas nuestro proyecto Django, pero con el problema *DisallowedHost*, problema del cual no nos tendremos que preocupar dado que lo solucionaremos en los pasos que realizaremos posteriormente. Ahora mismo, solamente deberemos alegrarnos con que acceda a nuestro proyecto Django sin problemas, si es así, podremos seguir con los pasos que veremos a continuación. Si no, tendremos que realizar nuevamente los pasos nombrados anteriormente.

#### Creación del archivo .gitignore 
Inmediatamente después de que hayamos visualizado que nuestro proyecto Django está funcionando, pasaremos a crear el fichero *.gitignore*, fichero donde introduciremos todos los directorios y ficheros que finalmente no querremos que se suban a nuestro repositorio Git, porque recordemos que, una de las características para una producción segura es la de tener nuestro proyecto bajo un VCS.
Por dicha razón, ejecutemos los siguientes comandos en nuestra máquina virtual para la creación de este fichero:
```
1. cd ..
2. sudo nano .gitignore
```
E introduciremos lo siguiente en el archivo *.gitignore*:
```
*.pyc
/[nombre_de_tu_entorno_virtual]/
/venv/
/static/*
/media/*
.env
db.sqlite3
```
Hecho esto, ya tendremos nuestro fichero *.gitignore* listo para cuando subamos nuestro proyecto a nuestro repositorio Git.

#### Instalación de django-environ y requirements.txt
Una vez que tengamos nuestro fichero *.gitignore* listo, pasaremos a instalar la librería *django-environ*, librería que cuya función será la de pasar datos sensibles de la aplicación que crearemos mediante variables de entorno, consiguiendo así, una mayor seguridad, ya que, dicha información sensible no se mostrará de una manera explícita.
Explicado esto, instalaremos dicha librería ejecutando el siguiente comando en nuestra máquina virtual:
```
1. pip install django-environ
```
Instalada de manera exitosa la librería *django-environ*, produciremos el fichero *requirements.txt*, fichero encargado de contener todas las versiones de las librerías que instalemos en nuestro entorno virtual y en el cual deberemos añadir la versión de cada una de las librerías que instalemos para que tengamos claro en todo momento las librerías utilizadas en nuestro proyecto. Por dicha razón, como anteriormente y ahora hemos instalado algunas librerías, es el momento perfecto para crear dicho fichero con todas las versiones de nuestras librerías. Por ello, tendremos que ejecutar los siguientes comandos:

*(El segundo comando que ejecutemos, solamente será para visualizar todas las versiones de las librerías que tengamos instaladas. Y el cuarto, para visualizar si el archivo requirements.txt se ha creado con éxito.)*

```
1. cd mysite
2. pip freeze
3. pip freeze > requirements.txt
4. ls
```
Realizado todos estos comandos sin problemas, podremos continuar con la creación de nuestro proyecto Django.

#### Modificación del archivo settings.py
Instalada la librería *django-environ* y creado el fichero *requirements.txt* con las respectivas versiones de las librerías que tenemos instaladas, deberemos modificar el archivo *settings.py* de nuestro proyecto, indicándole las variables de entorno que posteriormente configuraremos y solucionando el problema que teníamos de *DisallowedHost*. Comentado esto, accederemos al archivo *settings.py* ejecutando los siguientes comandos:
```
1. cd mysite
2. sudo nano settings.py
```
Y reemplazaremos todo su contenido por el siguiente:
```
"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ALLOWED_HOSTS = [ '*', ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```
Cuando finalicemos, guardaremos los cambios con la combinación de teclas Control + O y saldremos con Control + X.

#### Creación del fichero .env
Modificado unos de los puntos del archivo *settings.py* (porque sí, deberemos modificar alguna cosa más después), pasaremos a crear el fichero *.env*, fichero que contendrá las variables de entorno de nuestra aplicación Django, en el cual deberemos añadir las variables DEBUG y SECRET_KEY ya indicadas en el fichero *settings.py*, para que así la modificación que hemos realizado tenga efecto.

Sabiendo esto, pasaremos a crear el fichero *.env* ejecutando el siguiente comando:
```
1. cd ..
2. sudo nano .env
```
Y añadiremos por el momento las siguientes variables de entorno:
```
SECRET_KEY=nombre_que_tu_quieras
DEBUG=True
```
Añadidas las variables de entorno en el fichero *.env*, guardaremos los cambios con la combinación de teclas Control + O y saldremos de el con la combinación de teclas Control + X.

#### Instalación, configuración y verificación de MySQL
Una vez que tengamos nuestro fichero *.env* y ya hayamos añadido las variables de entorno SECRET_KEY y DEBUG, procederemos a pasar a instalar los binarios necesarios para la instalación de MySQL. Para ello, ejecutaremos el siguiente comando:
```
1. sudo apt install libmysqlclient-dev gcc python3-dev python3-mysqldb -y
```
Posteriormente, instalaremos los conectores de MySQL para nuestro entorno virtual Python ejecutando el comando siguiente:
```
1. pip install mysqlclient
```
Cuando finalice la instalación de los conectores MySQL, instalaremos ahora sí, el paquete de MySQL, para ello ejecutaremos el comando siguiente:
```
1. sudo apt install mysql-server -y
```
Para comprobar si la base de datos MySQL está funcionando correctamente, ejecutaremos el comando que veremos ahora a continuación, que se encargará de crear las tablas necesarias en caso de que nuestra base de datos este vacía (que en este caso si lo estará, porque es una instalación totalmente de cero):
```
1. python3 manage.py migrate
```
Cuando ejecutemos dicho comando, veremos que nos aparecerá un mensaje de error, que no cunda el pánico, esto se debe a que debemos ajustar también las variables de entorno para nuestra base de datos MySQL en el archivo *settings.py* y añadirla en el fichero *.env*. Para hacer todo esto, vayamos primero a modificar lo necesario en el fichero *settings.py*:
```
1. cd mysite
2. sudo nano settings.py
```
Dentro del fichero *settings.py*, deberemos reemplazar esto:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
Por esto:
```
DATABASES = {
    'default': env.db(),
}
```
Cuando hayamos realizado los cambios, los guardaremos la combinación de teclas Control + O y saldremos del fichero con Control + X.

Hecho esto, ahora deberemos crear una base de datos llamada *polls* y un usuario con total privilegios en dicha base de datos en nuestro MySQL. Todo esto lo realizaremos para tenerlo listo para cuando produzcamos posteriormente nuestra aplicación.
Dicho esto, para realizar lo comentado deberemos ejecutar los siguientes comandos:
```
1. sudo mysql
2. CREATE DATABASE polls;
3. CREATE USER 'nombre_que_queremos_asignarle_a_nuestro_usuario_administrador'@'localhost' IDENTIFIED BY 'contraseña_que_nosotros_queramos';
4. GRANT ALL PRIVILEGES ON *.* TO 'nombre_del_usuario_que_acabamos_de_crear'@'localhost';
5. exit
```
Una vez finalicemos la creación de nuestra base de datos *polls* y del usuario administrador de dicha base de datos, pasaremos a introducir la variable de entorno de la base de datos en el fichero *.env*. Para ello, ejecutaremos los siguientes comandos:
```
1. cd mysite
2. sudo nano .env
```
Y añadiremos la variable de entorno de nuestra base de datos en dicho fichero:
```
DATABASE_URL='mysql://nombre_de_nuestro_usuario_administrador:su_contraseña@localhost:3306/polls'
```
Añadida la variable de entorno de nuestra base de datos en el fichero *.env*, guardaremos los cambios con la combinación de teclas Control + O y saldremos de el con Control + X.

Por último, ejecutaremos nuevamente el comando:
```
1. python3 manage.py migrate
```
Y ahora sí, visualizaremos que ahora no nos aparecerá ningún tipo de error y las tablas se habrán creado correctamente.

#### Creación y configuración de la aplicación Polls
En el momento que tengamos nuestra base de datos *polls* creada correctamente, hayamos cargado las tablas y estén preparadas las variables de entorno en el fichero *settings.py* y en el *.env*, podremos proceder a la creación y a la configuración de nuestra aplicación Django que llamaremos *polls*. 
En primer lugar, empezaremos con la creación de la aplicación polls, para ello ejecutaremos el siguiente comando:
```
1. python3 manage.py startapp polls
2. ls
```
Una vez que ejecutemos el comando *ls* y visualizemos que nuestra aplicación *polls* se ha creado exitosamente, pasaremos a configurar a algunos de esos ficheros para conseguir que nos cargue las vistas que nosotros deseemos.

Para comenzar, deberemos acceder al archivo *polls/views.py*, archivo que contendrá el contenido inicial de nuestra aplicación, es decir, será nuestra vista principal proporcionando la bienvenida a los visitantes. Dicho esto, podremos acceder a dicho archivo de la siguiente manera:
```
1. sudo nano polls/views.py
```
Dentro de este fichero, deberemos eliminar todo el contenido que tenga y añadirle esté siguiente:
```
from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Hola, mundo! Te encuentras en el índice de POLLS.")
```
Cuando finalicemos de añadirlo, guardaremos los cambios con la combinación de teclas Control + O y saldremos del archivo con Control + X.

Seguidamente, crearemos al archivo *polls/urls.py*, archivo encargado de direccionar las vistas de nuestra aplicación. En este caso, deberemos añadir la ruta de la vista que hemos creado anteriormente, para que así cuando arranquemos nuestro servidor con nuestra aplicación Django nos redirija correctamente donde queremos. Comentado esto, generaremos dicho archivo con el comando siguiente:
```
1. sudo nano polls/urls.py
```
Y añadiremos lo siguiente:
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
Cuando finalicemos de añadir dicho contenido, guardaremos los cambios con la combinación de teclas Control + O y saldremos del archivo con Control + X.

Seguidamente, también deberemos hacer algo parecido con el archivo *mysite/urls.py*, pero esta vez en vez de generarlo, solamente deberemos acceder a él, ya que, en *mysite* dicho archivo ya está creado. Para acceder a dicho archivo ejecutaremos el siguiente comando:
```
1. sudo nano mysite/urls.py
```
Y cambiar todo su contenido por este siguiente:
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```
Como siempre, cuando finalicemos de añadir el contenido necesario, guardaremos los cambios con la combinación de teclas Control + O y saldremos del archivo con Control + X.

En seguida, procederemos a crear unos modelos de encuesta para nuestra aplicación *polls*, dado que, por ahora de esto tratará nuestra aplicación. Teniendo esto en cuenta, pasaremos a realizar los modelos de encuesta. Para ello, accederemos al archivo *polls/models.py* ejecutando el siguiente comando:
```
1. sudo nano polls/models.py
```
Y cambiaremos todo su contenido por el siguiente:
```
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
Y como ya sabremos, cuando terminemos de añadir el contenido correspondiente, guardaremos los cambios con la combinación de teclas Control + O y saldremos del archivo con Control + X.

Posteriormente, deberemos dirigirnos nuevamente a nuestro fichero *mysite/settings.py* y añadir la siguiente línea *'polls.apps.PollsConfig',* en el apartado *INSTALLED_APPS*, para que posteriormente podamos incluir esta aplicación a nuestro proyecto Django. Para ello, deberemos ejecutar el siguiente comando:
```
1. sudo nano mysite/settings.py
```
Y añadir lo siguiente línea *'polls.apps.PollsConfig',* en el apartado INSTALLED_APPS, quedando una cosa como está:
```
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
``` 
Cuando terminemos de añadir el contenido correspondiente, guardaremos los cambios con la combinación de teclas Control + O y saldremos del archivo con Control + X.

Ulteriormente, añadiremos la app Polls a nuestro proyecto Django ejecutando el siguiente comando:
```
1. python3 manage.py makemigrations polls
```
Y haremos la migración de las tablas MySQL de dicha aplicación con los comandos siguientes:
```
1. python3 manage.py sqlmigrate polls 0001
2. python3 manage.py migrate
```
Ya casi acabando con nuestra aplicación *polls*, crearemos un superusuario para poder acceder a la vista de administración de nuestra app. Para hacerlo, deberemos ejecuta el siguiente comando:
```
1. python3 manage.py createsuperuser
```
*(Posteriormente, deberemos rellenar con nuestros respectivos datos lo que nos solicite el asistente)*

Ya por último, acabaremos con la configuración de nuestra aplicación *polls* arrancando nuestro servidor Django y visualizando a través de nuestro navegador web si podemos acceder correctamente a todas la vistas. Para iniciar nuestro servidor recordemos que deberemos ejecutar el siguiente comando:
```
1. python3 manage.py runserver 0.0.0.0:8000
```
Y accederemos a través de nuestro navegador web a nuestro servidor web añadiendo la dirección IP de nuestra máquina virtual, el puerto 8000. Introduciendo una cosa así:
```
nuestra_dirección_IP:8000
```
*(En este caso, nos aparecerá la vista principal, es decir, en la que visualizaremos la frase; ¡Hola, mundo! Te encuentras en el índice de POLLS.)*

En cambio, si buscamos lo siguiente:
```
nuestra_dirección_IP:8000/admin
```
*(Deberemos visualizar el inicio de sesión de nuestra aplicación polls, en el cual podremos introducir las credenciales del superusuario que creamos anteriormente para poder acceder.)

#### Instalando y poniendo en marcha nuestro servidor de aplicaciones uWSGI
En el tiempo que hayamos comprobado que todas las vistas de nuestra aplicación Django están funcionando correctamente, pasaremos a utilizar la herramienta *uWSGI*. Esta herramienta se encargará de ser nuestro servidor de aplicaciones e indicarle a nuestro servidor web (Nginx) como se tiene que comunicar con nuestra aplicación web, consiguiendo de esta manera, llegar a poder encadenar diferentes aplicaciones web para procesar una solicitud o una petición.
Dicho esto, instalaremos esta herramienta en nuestro entorno virtual y hacer una pequeña prueba poniendo nuestra aplicación web en marcha a partir de este servidor web. Para realizar esto, ejecutaremos los siguientes comandos:
```
1. pip install uwsgi
2. uwsgi --http :8000 --module mysite.wsgi
```
Una vez pongamos en marcha nuestra aplicación web, podremos acceder nuevamente a través de alguno de nuestros navegadores web a ella introduciendo la dirección IP de nuestra máquina virtual y su puerto 8000. También podremos acceder a las diferentes vistas para comprobar que funcionan correctamente:

(Recordamos que, deberemos encontrarnos en el directorio de mysite para que no tengamos problemas a cargar nuestro contenido. Comando para acceder a mysite —> cd /home/vagrant/mysite)

```
nuestra_dirección_IP:8000
nuestra_dirección_IP:8000/admin
```
Como visualizaremos, las vistas nos aparecerá sin ningún estilo CSS, ni imágenes, etc. Y esto es debido a que nuestro servidor web Nginx no está cargando correctamente los archivos estáticos de nuestra aplicación web, es decir, lo nombrado anteriormente, CSS, imágenes, etc. Por dicha razón, no nos tendremos que alarmar por ello y, continuar con el siguiente punto para solucionar este pequeño problema y hacer funcionar nuestra aplicación web con su respectivo estilo.

#### Instalación y configuración de nuestro servidor web Nginx para cargar archivos estáticos
Ulteriormente de que hayamos comprobado que nuestro servidor de aplicaciones web uWSGI esta funcionando correctamente y nos cargue nuestro contenido (aunque sin estilo), procederemos a hacer todo lo necesario para hacer lo nombrado en el punto anterior, cargar los archivos estáticos de nuestra aplicación para que se visualice de la manera correcta. 

En primer lugar, deberemos instalar e iniciar nuestro servidor web Nginx para poder realizar las configuraciones pertinentes para que nuestra aplicación web funcione correctamente. Para ello, deberemos ejecutar el comando que veremos a continuación:
```
1. sudo apt install nginx -y
2. sudo /etc/init.d/nginx start 
```
En segundo lugar, nos deberemos dirigir al directorio donde Nginx guarda las configuraciones de los contenidos de nuestras aplicaciones web, para así poder realizar el nuestro. Dicho directorio es */etc/nginx/sites-available*, y deberemos ejecutar el siguiente comando para acceder a él:
```
1. cd /etc/nginx/sites-available
```

Dentro de este directorio crearemos un archivo *.conf* con el nombre que nosotros queremos ejecutando el comando siguiente:
```
1. sudo nano mysite.conf
```
Seguidamente, dentro de este archivo de configuración, añadiremos la siguiente configuración indicando nuestras rutas correspondientes:
```
# mysite_nginx.conf

# the upstream component nginx needs to connect to
upstream django {
    # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
    server 127.0.0.1:8001; # for a web port socket (we'll use this first)
}

# configuration of the server
server {
    # the port your site will be served on
    listen      8000;
    # the domain name it will serve for
    server_name example.com; # substitute your machine's IP address or FQDN
    charset     utf-8;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
    location /media  {
        alias /ruta/de/tu/proyectoDjango/media;  # your Django project's media files - amend as required
    }

    location /static {
        alias /ruta/de/tu/proyectoDjango/static; # your Django project's static files - amend as required
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     /ruta/de/tu/proyectoDjango/uwsgi_params; # the uwsgi_params file you installed
    }
}
```
En mi caso serán las siguientes:
```
# mysite_nginx.conf

# the upstream component nginx needs to connect to
upstream django {
    # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
    server 127.0.0.1:8001; # for a web port socket (we'll use this first)
}

# configuration of the server
server {
    # the port your site will be served on
    listen      8000;
    # the domain name it will serve for
    server_name example.com; # substitute your machine's IP address or FQDN
    charset     utf-8;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
    location /media  {
        alias /home/vagrant/mysite/media;  # your Django project's media files - amend as required
    }

    location /static {
        alias /home/vagrant/mysite/static; # your Django project's static files - amend as required
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     /etc/nginx/uwsgi_params; # the uwsgi_params file you installed
    }
}
```
Cuando finalicemos de añadir nuestra respectiva configuración, guardaremos los cambios con la combinación de teclas Control + O y saldremos de él con Control + X.

Posteriormente, cuando nuestra configuración esté guardada correctamente, procederemos a realizar un enlace simbólico de nuestro sitio web para que nuestro servidor web Nginx pueda verlo y procesarlo de manera correcta. Para ello, ejecutaremos el siguiente comando:
```
1. sudo ln -s /etc/nginx/sites-available/nombre_de_nuestro_archivo_de_configuracion.conf /etc/nginx/sites-enabled/
```
Hecho este enlace simbólico sin problemas, deberemos dirigirnos nuevamente al archivo de configuración *settings.py* de nuestro proyecto Django *mysite* y, añadir las variables *STATIC_ROOT* y *STATIC_URL* con las respectivas rutas donde se encuentran nuestros archivos estáticos. Para realizar esto, tendremos que ejecutar el siguiente comando:
```
1. sudo nano /home/vagrant/mysite/mysite/settings.py
```
Y añadir la variable *STATIC_ROOT* y su ruta casi al final del archivo donde se encuentra la variable *STATIC_URL*, y modificar la ruta de la variable *STATIC_URL*. La variable *STATIC_ROOT*, la podremos poner tanto arriba o abajo de la variable *STATIC_URL*, el orden no influirá en nada. Comentado esto, deberá quedar una cosa así:
```
STATIC_ROOT = 'static/'
STATIC_URL = '/static/'
```
Ya casi acabando, cuando hayamos añadido y modificado las variables nombradas anteriormente, guardaremos los cambios con la combinación de teclas Control + O y saldremos con Control + X. Hecho esto, deberemos cargar los archivos estáticos de nuestra aplicación web para que la visualicemos de la forma correcta y reiniciar nuestro servidor web Nginx para que se apliquen todos los cambios. Para ello ejecutaremos los siguientes comandos:
```
1. cd /home/vagrant/mysite
2. python3 manage.py collectstatic 
3. sudo /etc/init.d/nginx restart
```
Realizado todo estos pasos sin problemas, ya podremos seguir con el paso siguiente en donde iniciaremos nuestra aplicación web *polls* con éxito ;).

#### Iniciación de nuestra aplicación web polls de manera correcta
Ya casi acabando, solamente nos quedará arrancar nuestro socket en nuestro servidor de aplicacionesuWSGI para que así podamos visualizar nuestra aplicación web con sus respectivos archivos estáticos.
Dicho esto, ejecutemos el comando necesario para arrancar nuestro socket:

*(Recordamos que, deberemos encontrarnos en el directorio de mysite para que no tengamos problemas a cargar nuestro contenido. Comando para acceder a mysite ---> cd /home/vagrant/mysite)*

```
1. uwsgi --socket :8001 --module mysite.wsgi
```
Hecho esto, podremos acceder a cualquiera de nuestras vistas y visualizar que la interfaz gráfica será mucho más bonita, dado que, los archivos estáticos que indicamos se han ejecutado correctamente.

Si esto es así, ¡ENHORABUENA! Ya tenemos nuestra aplicación web funcionando correctamente.

#### Subir nuestro proyecto Django a nuestro VCS Git
Ya por último, subiremos nuestro proyecto Django a un VCS, en mi caso, explicaré como hacerlo en VCS Git, ya que, es el que siempre utilizo, pero si vosotros sabéis subirlo y queréis utilizar otro VCS lo podréis hacer sin problemas.
Dicho esto, seguiremos los siguientes pasos para lograr subir nuestro proyecto a un repositorio Git:
1. En primer lugar, deberemos dirigirnos a la [página web oficial](https://github.com/) de Git e iniciar sesión con nuestra cuenta (si no tenemos cuenta, podremos registrarnos totalmente gratis).
2. En segundo punto, deberemos crear un repositorio nuevo para guardar los archivos de nuestro proyecto. Para ello, deberemos pinchar con clic izquierdo encima de la foto de nuestro perfil y seleccionar la opción de *Your repositories*. Una vez nos encontremos en dicha opción, presionaremos con clic izquierdo en el botón llamado *New* y después rellenaremos los campos con nuestros datos correspondientes (rellenar campos obligatorios). Cuando finalicemos de rellenar los campos, crearemos nuestro repositorio dándole clic izquierdo a *Create repository*.
3. Posteriormente, solo nos faltará ejecutar los siguientes comandos:

    *(Recordamos que, deberemos encontrarnos en el directorio de /home/vagrant para poder subir correctamente todo el contenido de mysite a nuestro VCS Git. Comando para acceder a /home/vagrant ---> cd /home/vagrant)*
    ```
    1. git init
    2. git add mysite
    3. git config --global user.email "nuestro_correo_eléctronico"
    4. git config --global user.name "nombre_de_usuario_de_nuestra_cuenta_Git"
    5. git commit -m "insertamos_el_comentario_que_queramos"
    6. git branch -M main
    7. git remote add origin enlace_de_nuestro_repositorio
    8. git push -u origin main
    ```
Después, introduciremos nuestro nombre de usuario de Git y el token de nuestra cuenta, y presionaremos la tecla *Enter* para proceder a subir nuestro proyecto al repositorio seleccionado de Git.
*(Cabe recalcar que, el token podremos generarlo en el apartado Settings de nuestra cuenta.)*

Realizado esto sin problemas, ya tendremos nuestro repositorio con el proyecto de nuestra aplicación Django subida con éxito. ¡ENHORABUENA! Habrás conseguido hacer una aplicación web de Django de manera adecuada y segura.






 




