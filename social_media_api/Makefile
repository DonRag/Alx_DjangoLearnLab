project:
	django-admin startproject $(name) $(dir)

server:
	python manage.py runserver

app:
	python manage.py startapp $(name)

mk:
	python manage.py makemigrations

migrate:
	python manage.py migrate

shell:
	python manage.py shell

flush:
	python manage.py flush

super:
	python manage.py createsuperuser 

pipu:
	pip install --upgrade pip

depnd:
	pip install django mysqlclient python-dotenv djangorestframework djangorestframework-simplejwt django-filter black
	
format:
	black $(dir)