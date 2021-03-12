from django.shortcuts import render
from django.http import HttpResponse 
#wan to import randomness when creating a pass
import random 



# the user will request to go to the home page
# we need to provide a response in the form of HTTP
#this will take the user to a page that will say hello there friend 

#render is a function from django that allows us to pass back a template, that turns into a http response 

#password  is dictionar key map that can be referenced inside of the home.html file
def home(request):
    return render(request,'generator/home.html')

#eggs page
def password(request):
    #varaible to hold in the passWord 
    thePassWord = ''
    #takes this string and breaks it up into an array
    characters = list('abcdefghijklmnopqrstuvwxyz')
    #length of the password
    length = 10
    for x in range(length):
        thePassWord += random.choice(characters)
    
     
    return render(request,'generator/password.html', {'password':thePassWord})