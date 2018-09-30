__author__ = 'DELL'
from django.urls import path
from django.conf.urls import url
from .import  views

app_name="Teachers"

urlpatterns=[
    path('mainprofile',views.mainprofile,name="mainprofile"),
    url(r'^editprofile',views.editprofile,name="editprofile"),

]