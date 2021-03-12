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
    #get the length requested by the user
        #integers conversion, gets the value from length passed on by the user in the following page
        #becomes the overall length of the new string
    
    #UPPER CASE LETTERS
    #check to see if the user is requesting uppercase letters
        #if they do add the capital letters to the already lower case list
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))     
    #SPECIAL LETTERS
    #add special letters to the list
    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*()_+-\[];?>.<,~'))
    #Numbers
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
        
    length = int(request.GET.get('length',12)) #12 represents the default value
    for x in range(length):
        thePassWord += random.choice(characters)
    
    return render(request,'generator/password.html', {'password':thePassWord})

def aboutMe(request):
    return render(request, 'generator/aboutMe.html')