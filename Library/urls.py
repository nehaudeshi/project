__author__ = 'DELL'

from django.urls import path
from .import views

app_name='Library'

urlpatterns = [

    path('Technology',views.tech,name="tech"),
    path('Chemical',views.chem,name="chem"),
    path('Biotechnology',views.bio,name="bio"),
    path('Electronics',views.elec,name="elec"),
    path('Mechanical',views.mech,name="mech"),

]

