# Step by Step Manual Instructions

1. cd E:\python_dev\django
2. python -m venv venv_django
3. cd E:\python_dev\django\venv_django\Scripts
4. activate
5. pip install django
6. cd E:\python_dev\django
7. django-admin startproject hello_django
8 cd E:\python_dev\django\hello_django
9. django-admin startapp core 
10. hello_django --> settings.py
add 'core' to installed_apps

11. Edit your_app_name --> core --> views.py to import HttpResponse
from django.shortcuts import render, HttpResponse

12. Create your functions here your_app_name --> core --> views.py 
def hello(request, name, age):
    return HttpResponse('<h1>Hello {}, you are {} years old <h1>'.format(name, age))

13. Edit your_app>your_app>urls.py
14. add the line below to import views:
     from core import views

    path('hello/<name>/<age>', views.hello),