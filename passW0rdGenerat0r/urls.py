"""passW0rdGenerat0r URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
#need the views file from generator
from generator import views

#not using admin so i can get rid of that 

#home page - want to customize where the user goes for a home page so we set the path to home
# views.home is a function, but its also what will appear on the page and it  will send the user to a page and whats displaced on views .py will appear as the page
#same with views.eggs
urlpatterns = [
    path('', views.home, name ="home"),
    path('generatedpassword/', views.password, name="password"),
    path('aboutMePage/', views.aboutMe, name = "aboutMe"),
]
