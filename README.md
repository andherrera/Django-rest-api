# Django-rest-api
A CRUD REST API with Python [Django Rest Framework](https://www.django-rest-framework.org) and JSON Web Token [JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html) authentication. This application also includes the following features:

**Key Features**
* Register
* Login
* Password Validation
* CRUD Application
* Logging
* Pagination
* Unit test
* Python requests module

## Requirements

* Python 3.11.0
* Django 3.2.7
* Django REST Framework 3.12.4
* Requests 2.28.2

## ER Diagram

![Screenshot_1](https://user-images.githubusercontent.com/65980778/214958240-add500a5-8d6d-4932-8069-802e3e21992d.png)

## Endpoints

Endpoint | HTTP Method | Description
| :--- | :---: | :---:
`/user/`  | POST | Register User
`/login/`  | POST | User login
`/movies/`  | POST | Create movie
`/movies/`  | GET | Retrieve all movies
`/movies/:id`  | GET | Retrieve a single movie
`/movies/:id`  | PUT | Modify a single movie
`/movies/:id`  | DELETE | Delete a single movie

## Installation

After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command

```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running

```
pip install -r requirements.txt
```

## Running the Application

Before running the application we need to create the needed DB tables:
```
python ./manage.py makemigrations
```
```
python ./manage.py migrate
```
Start the server
```
python ./manage.py runserver
```
Django will start running the server at localhost port 8000



