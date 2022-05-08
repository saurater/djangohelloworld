# Step by Step Manual Instructions

1. cd E:\python_dev\django 
  <br> (make sure the djangohelloworld.py and djangosetup.py files are in this folder - You can change its name / path)
4. python -m venv venv_django
5. cd E:\python_dev\django\venv_django\Scripts
6. activate
7. pip install django
8. cd E:\python_dev\django
9. django-admin startproject hello_django
10. cd E:\python_dev\django\hello_django
11. django-admin startapp core 
12. hello_django --> settings.py
      <br>   add 'core' to installed_apps

11. Edit your_app_name --> core --> views.py to import HttpResponse


from django.shortcuts import render, HttpResponse

12. Create your functions here your_app_name --> core --> views.py
 
    def hello(request, name, age):
  
       return HttpResponse('Hello {}, you are {} years old >'.format(name, age))

13. Edit your_app>your_app>urls.py
14. add the line below to import views:
     from core import views

    path('hello/<name>/<age>', views.hello),
      
15. cd E:\python_dev\django\hello_django
16. python manage.py runserver
17. In your browser go to http://127.0.0.1:8000/hello/name/age
      
