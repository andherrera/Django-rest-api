# :movie_camera: Movies Django-rest-api 
A CRUD REST API with Python [Django Rest Framework](https://www.django-rest-framework.org) and JSON Web Token [JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html) authentication.

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
`/refresh/` | POST | Refresh Access Token
`/movies/`  | POST | Create movie
`/movies/`  | GET | Retrieve all movies
`/movies/:id`  | GET | Retrieve a single movie
`/movies/:id`  | PUT | Modify a single movie
`/movies/:id`  | DELETE | Delete a single movie
`/randNum/`  | GET | Retrieve a random number from a public Endpoint

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

## Testing the Application

The following tests were performed using [Postman](https://www.postman.com/downloads/). 

### Register User

![postu](https://user-images.githubusercontent.com/65980778/215204500-72c973d1-84cf-4104-a5d9-f95083bdcbfa.png)

### User login

![login](https://user-images.githubusercontent.com/65980778/215204497-eae81bc8-b79e-4fbc-977d-c00c8a195e44.png)

### Refresh Token

![refresh](https://user-images.githubusercontent.com/65980778/215204495-ec3d67ab-6243-4391-8fda-14d00ab11fe8.png)

The following requests must include the access token.

![auth](https://user-images.githubusercontent.com/65980778/215206817-a47e8fd2-8dcd-425e-8c46-af99bd6af51e.png)

### Post movie

![createmovie](https://user-images.githubusercontent.com/65980778/215204492-1e485933-6384-408b-ae71-548495ecabe9.png)

### Get all movies

![getMovies](https://user-images.githubusercontent.com/65980778/215204489-394df3f9-6737-4d8c-999d-cda0279a324b.png)
![pagination](https://user-images.githubusercontent.com/65980778/215204487-8e0ca40d-9ddc-40b4-8cee-b3352d1982be.png)

### Get a single movie

![getonemovie](https://user-images.githubusercontent.com/65980778/215204485-14e469f2-0896-479e-95ba-127136336c49.png)

### Put a single movie

![putmovie](https://user-images.githubusercontent.com/65980778/215204483-f3050441-d69a-4f54-92ff-ba955f853434.png)
![afterPut](https://user-images.githubusercontent.com/65980778/215204480-244558e0-7ad8-47ed-9863-79334714efd3.png)

### Delete a single movie

![deeletemovie](https://user-images.githubusercontent.com/65980778/215204477-3b5a2918-5030-4733-b21b-511b5a79d6a8.png)

### Get Tandom Number public API

![randNum](https://user-images.githubusercontent.com/65980778/215204473-90d2b124-176c-41f7-a9fa-58422455a14c.png)

### Logging

![logs](https://user-images.githubusercontent.com/65980778/215204502-42110d38-140c-43f3-a87e-c50c5a2a685b.png)

### Unit test

In order to run the test unit, use the command below
```
python ./manage.py test
```





