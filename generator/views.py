from django.shortcuts import render
from django.http import HttpResponse 



# the user will request to go to the home page
# we need to provide a response in the form of HTTP
#this will take the user to a page that will say hello there friend 

#render is a function from django that allows us to pass back a template, that turns into a http response 

#password  is dictionar key map that can be referenced inside of the home.html file
def home(request):
    return render(request,'generator/home.html', {'password':'apples'})

#eggs page
def eggs(request):
    return HttpResponse('<h1>Arrepas y huevos</h1>')