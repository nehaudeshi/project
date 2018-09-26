from django.shortcuts import render
import pyrebase
from django.db import models
from firebase_admin import credentials
from WEBSITE.models import registertable

def mainprofile(request):
    
    return  render(request,'Teachers/mainpage.html')
    
def editprofile(request):
    
        
    return render(request,'Teachers/editpage.html')

        


