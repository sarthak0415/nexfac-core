### Followed this tutorial
https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c

### Virtual environments

```
$ sudo apt-get install python-virtualenv
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install --upgrade pip
$ pip install django
$ pip install djangorestframework
```

### Create new project
```
django-admin startproject nexfac_core
cd nexfac_core
python manage.py runserver

python manage.py startapp nexfac_core_api
```

### DB migrate and superuser creation
```
python manage.py migrate
python manage.py createsuperuser

Email address: admin@nexfac.com
Password: coffee@321
```


### Tasks left -
1. Add support for independent tasks
2. Return tasks for users, currently only user details are returned