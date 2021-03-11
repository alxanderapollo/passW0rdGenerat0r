from django.shortcuts import render
from django.http import HttpResponse 



# the user will request to go to the home page
# we need to provide a response in the form of HTTP
#this will take the user to a page that will say hello there friend 
def home(request):
    return HttpResponse('Hello there friend')

#eggs page
def eggs(request):
    return HttpResponse('<h1>Arrepas y huevos</h1>')