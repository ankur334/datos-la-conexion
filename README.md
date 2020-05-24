# datos-la-conexion

This is a independent web service which creates connection from different data sources like Databases, Cloud and Files.
This project can be used to learn Full Stack Development with Django Rest Frame for backend and Vue.js for frontend.

## Getting Started


### Prerequisites
We have tested this project on Debian based Linux system. It will work absolutely fine on other OS too, 
but you will need to search the internet and fix the issue at time of installation of inbuilt library used.

```
1). Operating System - Debian or Ubuntu. 
2). Python(3.6)
```

### Installing
We will use Django for creating our backend for the system. Django is written in Python. We need Python to do 
anything in Django. Let's start by installing it! We want you to install the latest version of Python 3, 
so if you have any earlier version, you will need to upgrade it. We will using python 3.6 for this project.

* Installing Python.

```
sudo apt install python3
```
Verify the installation was successful by opening a command prompt and running the `python3` command:
 
```
python3 --version
```

* Virtual environment

Before we install Django we will get you to install an extremely useful tool to help keep your coding environment tidy 
on your computer. It's possible to skip this step, but it's highly recommended. Starting with the best possible setup 
will save you a lot of trouble in the future! So, let's create a virtual environment (also called a virtualenv). 
Virtualenv will isolate your Python/Django setup on a per-project basis. This means that any changes you make to one 
website won't affect any others you're also developing. Neat, right?
All you need to do is find a directory in which you want to create the virtualenv; your home directory, for example. 
On Windows, it might look like C:\Users\Name\ (where Name is the name of your login).

For this tutorial we will be using a new directory `datos` from your home directory:
```
mkdir datos
cd datos
mkdir backend
cd backend
``` 

We will make a virtualenv called `myvenv`. The general command will be in the format:
```
python3 -m venv myvenv
```
`myvenv` is the name of your virtualenv. You can use any other name, but stick to lowercase and use no spaces. 
It is also a good idea to keep the name short as you'll be referencing it a lot!

NOTE: On some versions of Debian/Ubuntu you may receive the following error:
```
The virtual environment was not created successfully because ensurepip is not available.  On Debian/Ubuntu systems, 
you need to install the python3-venv package using the following command.
   apt install python3-venv
You may need to use sudo with that command.  After installing the python3-venv package, recreate your virtual environment.
```
NOTE: On some versions of Debian/Ubuntu initiating the virtual environment like this currently gives the following error
```
Error: Command '['/home/eddie/Slask/tmp/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1
```

To get around this, use the virtualenv command instead.
```
sudo apt install python-virtualenv
virtualenv --python=python3.6 myvenv
```
NOTE: If you get an error like
```
E: Unable to locate package python3-venv
```
then instead run:
```
sudo apt install python3.6-venv
```

* Working with virtualenv

The command above will create a directory called `myvenv` (or whatever name you chose) that contains our virtual 
environment (basically a bunch of directory and files).

* Linux and OS X
```
source myvenv/bin/activate
```

* For Windows
```
myvenv\Scripts\activate
```

* Installing Django
Now that you have your virtualenv started, you can install Django.

Before we do that, we should make sure we have the latest version of pip, the software that we use to install Django:

```
python -m pip install --upgrade pip
```
Installing packages with requirements
A requirements file keeps a list of dependencies to be installed using pip install:

First create a requirements.txt file inside of the `/datos/backend` folder. Your directory will 
look like this for now:

```
datos
├── backend
    └── requirements.txt
    └── myvenv
```
In your `requirements.txt` file you should add the following text:
```
Django==2.2
```
Now, run `pip install -r requirements.txt` to install Django. Your virtual environment must be on.


* Creating django project

We're going to start backend for our project.

The first step is to start a new Django project. Basically, this means that we'll run some scripts provided by Django 
that will create the skeleton of a Django project for us. This is just a bunch of directories and files that we will 
use later.

The names of some files and directories are very important for Django. You should not rename the files that we are 
about to create. Moving them to a different place is also not a good idea. Django needs to maintain a certain 
structure to be able to find important things.

```
Remember to run everything in the virtualenv. If you don't see a prefix (myvenv) or name that you have given to 
your virtual environement in your console, you need to activate your virtualenv. We explained how to do that in above 
section. Typing myvenv\Scripts\activate on Windows or source myvenv/bin/activate on Mac OS X or 
Linux will do this for you.
```

* Create project: OS X or Linux

In your Mac OS X or Linux console, you should run the following command. Don't forget to add the period 
(or dot) `.` at the end!
```
django-admin startproject datos .
```

* Create project: Windows

On Windows you should run the following command. (Don't forget to add the period (or dot) . at the end):
```
django-admin.exe startproject datos .
```

Once you finish this then you can check status of server or all these installation by running this following 
command.

```
python manage.py runserver
```
If this command work perfectly then you will not see any error in your terminal. Otherwise you can visit
this url to take help for installation of django project `https://tutorial.djangogirls.org/en/installation/`

* Setup Database

```bash
 sudo su - postgres
 psql
 CREATE DATABASE <datos_application>;
 CREATE DATABASE <datos_data>;
 CREATE USER <my-user-name> WITH PASSWORD 'password';
 GRANT ALL PRIVILEGES ON DATABASE <datos_application> TO <my-user-name>;
 GRANT ALL PRIVILEGES ON DATABASE <datos_data> TO <my-user-name>;
 \q
 exit
```

* Changing settings

Let's make some changes in `datos/settings.py`. Open the file using any of the code editor that you love.

In settings.py, find the line that contains `TIME_ZONE` and `LANGUAGE_CODE` and modify it to choose your own timezone. 

```.env
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'
```

We'll also need to add a path for static files. (We'll find out all about static files and CSS later in the tutorial.)
Go down to the end of the file, and just underneath the STATIC_URL entry, add a new one called STATIC_ROOT:

```.env
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

* Set up a database
There's a lot of different database software that can store data for your site. Django by default database `sqlite3` 
database but We'll use the `Postgres`.

Create one  `.env` file inside `backend` directory and copy following content to it.

```.env
{
    "default": {
        "NAME": "data_service",
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "DATABASE_TYPE": "postgres",
        "DATABASE": "datos_application",
        "USER": "<Database-user>",
        "PASSWORD": "<Password-of-datos_application>",
        "HOST": "localhost",
        "PORT": "5432"
    },
    "data": {
        "NAME": "data_service_data",
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "DATABASE_TYPE": "postgres",
        "DATABASE": "datos_data",
        "USER": "<Database-user>",
        "PASSWORD": "<Password-of-datos_data>",
        "HOST": "localhost",
        "PORT": "5432"
    }
}
```

There is already Database settings in your `datos/settings.py` file. Search for `DATABASE` key in your 
`datos/settings.py` file and replace this by following.

```.env
with open(os.path.join(BASE_DIR, 'datos', '.env')) as env_file:
    ENV_JSON = json.loads(env_file.read())

DATABASES = {
    'default': ENV_JSON['default'],
    'data': ENV_JSON['data'],
}
```

* Starting the web server
You need to be in the directory that contains the manage.py file (the backend directory). In the console, 
we can start the web server by running 

```
python manage.py runserver
```