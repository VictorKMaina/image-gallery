![alt text](static/images/logo.svg)

## An online photo gallery

### [Heroku Link](https://moringa-photos-app.herokuapp.com/) | [LucidCharts ERD](https://lucid.app/invitations/accept/29e27027-b8e7-4432-97f0-34935dbc4126) | [Figma Link](https://www.figma.com/file/sEPs8iUAxN4tVepLc2kwAA/Photos-Django-IP?node-id=0%3A1)

---
## Introduction

Photos is an online gallery app. You can upload photos, search for photos using categories, and filter them by location.

## Technologies Used

Photos is built on Django, a Python framework. The live app is deployed on Heroku, and Postgres is used to manage its database.

## Installation (Ubuntu)

You can run the app using a local server on your computer. You will need Git to clone the app from this repo. Since Photos also uses Python 3 and Postresql, you will need to install them on your machine.

```bash
$ sudo apt install git python3 postgresql
```

You can now clone the repository on your computer. Navigate into the new directory after the clone is complete.

```bash
$ git clone https://github.com/VictorKMaina/image-gallery.git
$ cd image-gallery
```
As mentioned before, Photos runs on Django and other Python modules. To install all the dependencies, you will need to create a virtual environment and activate it.

```bash
$ python3.8 -m venv env
$ source env/bin/activate
```

Note: Be sure to use your own preferred version of Python. You can confirm by running `$ python3 --version` on your terminal.

Next, install the dependencies from the `requirements.txt` file.

```bash
(env)$ pip install -r requirements.txt
```

Photos also makes use of a database, so you will need to create one using Postgres. You can find instrustions for creating a Postgresql user and password [here.](https://www.postgresql.org/docs/8.0/sql-createuser.html)

Enter Postgresql on your terminal using `psql`, then do

```postgres
username=# CREATE DATABASE photos;
username=# \q
```

The app looks for environment variables to run. To enable this, create a file in the app's root directory called `.env`.

```bash
(env)$ touch .env
```

Now go to `.env` and set the following environment variables.action-checkbox

```python
SECRET_KEY='<SECRET-KEY>'
DEBUG=True
DB_NAME='photos'
DB_USER='<postgres-username>'
DB_PASSWORD='<postgres-password>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS=['*']
DISABLE_COLLECTSTATIC=1
```

You now need to update your database to work with this app's models. Run the following on your terminal.

```bash
(env)$ python manage.py migrate
```

Run the application.

```bash
(env)$ python manage.py runserver
```

As long as the server is running, you can open it in the browser [using this link](http://127.0.0.1:8000).

## Tests

The app comes with some test cases. To run them, enter the following command in your terminal.

```bash
(env)$ python manage.py test
```

## Known bugs
At the moment, there are no known bugs.

## [LICENSE](/LICENSE)