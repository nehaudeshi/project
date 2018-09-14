__author__ = 'DELL'
from django.urls import path
from .import  views

app_name="Teachers"

urlpatterns=[
    path('mainprofile',views.mainprofile,name="mainprofile"),
    path('editprofile',views.editprofile,name="editprofile"),

]