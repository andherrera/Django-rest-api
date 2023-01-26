# Django-rest-api
A CRUD REST API with Python [Django Rest Framework](https://www.django-rest-framework.org).

## Requirements

* Python 3.11.0
* Django 3.2.7
* Django REST Framework 3.12.4

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

## ER Diagram

![alt text](https://drive.google.com/file/d/1jFALB4IO-_rv-_sOAV4bqmm0et_MM9GC/view?usp=sharing)



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




