#!/usr/bin/env python
"""
Django Hello World
Created on Tue May  3 08:46:40 2022
@author: Sam Faraday
Github: https://github.com/saurater/djangohelloworld

"""
import os

print("Welcome to My Django Hello World by Sam Faraday \n \n")

print("\n \n - - -> 1 Creating the folder structure - - - - - - - - - - - - - - \n \n ")
val = input("Please let me know where you'd like to install your Django Env: ")


print("\n ok. Let us create  the directory " + val + " for your \n")


path = os.path.join(val, "django")
os.mkdir(path)
print("\n Done. Folder created at " + path)

print("\n \n - - -> 2 Creating a Python Virtual Environment - - - - - - - - - - - - - - ")
print('\n Creating a Python Virtual Environment now... \n')

os.system("python -m venv " + path + "/venv_django")

print("\n Done. ")

print("\n \n - - -> 3 Activating the Python Virtual Environment - - - - - - - - - - - - - - ")
f= open( "djangopath.txt","w+")
f.write(path)
f.close

path = os.path.join(path + "\\venv_django\Scripts\\activate.bat")

print("\n 1. VENV has been created. To activate it, please copy and paste the following command: \n \n" + path)

print("\n 2. Then let us head for tne next step by copying and pasting the following command: \n")
print("python djangosetup.py")
