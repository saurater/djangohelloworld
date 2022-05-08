#!/usr/bin/env python
"""
Django Hello World / Setp up File
Created on Tue May  3 08:46:40 2022
@author: Sam Faraday
Github: https://github.com/saurater/djangohelloworld
"""

import os, time

print("\n \n - - -> 4 Installing Django - - - - - - - - - - - - - -  \n \n ")
print("\n Installing Django.... \n")

os.system("pip install django --quiet")

print("\n Django has been successfully installed \n")

f = open("djangopath.txt", "r")
if f.mode == 'r':
    path = f.read()
os.chdir(path)

#print("\n \n - - -> 5 Creating a Django Project - - - - - - - - - - - - - - ")
projectname: str = input("Please type your project name: ")
os.system('django-admin startproject ' + projectname)

f = open("djangoprojectname.txt", "w+")
f.write(path + "\\" + projectname)
f.close

os.chdir(path + "\\" + projectname + '\\' + projectname)

core_path = path + "\\" + projectname

""" Creating the Core the APP"""
os.chdir(path + "\\" + projectname)
os.system('django-admin startapp core')
os.chdir(path + "\\" + projectname + '\\' + projectname)

""" Adding the Core App to Settings.py """
#print("\n \n - - -> 6 Adding the new project app to the Settings.py - - - - - - - - - - - - - - ")
# Add the App to Settings.py
with open(os.getcwd() + '/settings.py', 'r') as file:
    filedata = file.read()

filedata = filedata.replace('django.contrib.staticfiles', 'django.contrib.staticfiles\', \n    \'core')

with open(os.getcwd() + '/settings.py', 'w') as file:
    file.write(filedata)

""" Creating the functions  """

""" Import HttpResponse """
os.chdir(path + "\\" + projectname + '\\core')

#print("\n \n - - -> 7 Creating the Function in views.py - - - - - - - - - - - - - - ")
# Add the App to Settings.py
with open(os.getcwd() + '/views.py', 'r') as file:
    filedata = file.read()

filedata = filedata.replace('from django.shortcuts import render', 'from django.shortcuts import render, HttpResponse')

with open(os.getcwd() + '/views.py', 'w') as file:
    file.write(filedata)

""" Create Functions """
os.chdir(path + "\\" + projectname + '\\core')

#print("\n \n - - -> 8 Creating the Function in views.py - - - - - - - - - - - - - - ")
# Add the App to Settings.py
with open(os.getcwd() + '/views.py', 'r') as file:
    filedata = file.read()

filedata = filedata.replace('# Create your views here.', '# Create your views here., \ndef hello(request, name, '
                                                         'age): \n return HttpResponse(\'<h1><center>Hello, {} , your are {} '
                                                         'years old </center>'
                                                         '<h1>\'.format(name, age))')

with open(os.getcwd() + '/views.py', 'w') as file:
    file.write(filedata)

""" 9. Setting up the urls.py file - Import"""
#print("\n \n - - -> 9 Setting up the urls.py file - - - - - - - - - - - - - - ")

os.chdir(core_path + '//' + projectname)

with open(os.getcwd() + '/urls.py', 'r') as file:
    filedata = file.read()

# Importing core
filedata = filedata.replace("from django.urls import path", "from django.urls import path \nfrom core import views")

with open(os.getcwd() + '/urls.py', 'w') as file:
    file.write(filedata)

"""10. Setting up the urls file - Setting the Functions path"""
#print("\n \n - - -> 10 Setting up the urls.py file - - - - - - - - - - - - - - ")

os.chdir(core_path + '\\' + projectname )

with open(os.getcwd() + '/urls.py', 'r') as file:
    filedata = file.read()

# Importing core
filedata = filedata.replace("path('admin/', admin.site.urls),", "path('admin/', admin.site.urls), \n   path("
                                                                "'hello/<name>/<age>', views.hello), \n   ")
with open(os.getcwd() + '/urls.py', 'w') as file:
    file.write(filedata)

print("\n \n  \n - - ->  Project Status - - - - - - - - - - - - - - ")
time.sleep(1)
print("\n So far we have \n")
time.sleep(1)

print("\n 1. Created the Folders Structure... \n")
time.sleep(1)
print("\n 2. Created a Python Virtual Environment... \n")
time.sleep(1)
print("\n 3. Activated the Virtual Environment... \n")
time.sleep(1)
print("\n 4. Installed Django... \n")
time.sleep(1)
print("\n 5. Created a Django Project... \n")
time.sleep(1)
print('\n 6. Added the new project app to the settings.py file  \n')
time.sleep(1)
print('\n 7. Creating the Function in views.py file \n')
time.sleep(1)
print('\n 8. Set up the urls.py file -  import \n')
time.sleep(1)
print('\n 9. Set up the urls.py file - Setting the Functions path \n')
time.sleep(1)
print('\n 10. Now... guess what... Let us run the server \n')
time.sleep(1)

os.chdir(core_path)
os.system("python manage.py runserver")

