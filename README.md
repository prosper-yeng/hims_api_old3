# HIMS_API
<app description here>

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [API Documentation](#api-documentation)
* [SuperAdmin Page](#superadmin-page)


## General info
<app description here>


## Technologies
* Python 3.10.6
* Django 4.0.5
* Django Rest Framework 3.13.1
* SQLite3 (on DEV)

### Setup
## Installation on Linux and Mac OS

* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo
* [Follow the guide here](http://simononsoftware.com/virtualenv-tutorial/) on how to create virtualenv

* To create a normal virtualenv (example .venv) and activate it (see Code below).

  ```
  virtualenv --python=python3.10.6 .venv
  
  source .venv/bin/activate

  (venv) $ pip install -r requirements.txt

  (venv) $ python manage.py makemigrations
 ```
 
 * provide appropriate values if the makemigrations step above demands

 ```
  (venv) $ python manage.py migrate

  (venv) $ python manage.py createsuperuser 

  (venv) $ python manage.py runserver
  ```
  
* Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).
* Open the address in the browser

## API Documentation
```
http://127.0.0.1:8000/schema
```

## SuperAdmin Page
```
http://127.0.0.1:8000/admin/
```