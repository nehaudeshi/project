from django.db import models
#from WEBSITE.models import registertable
class edit(models.Model):
	fname=models.CharField(max_length=300)
	lname=models.CharField(max_length=300)
	sapid=models.IntegerField()
	contact=models.IntegerField(max_length=10)
	email=models.EmailField(max_length=120)
	date=models.DateField()
	prof=models.CharField(max_length=600)




# Create your models here.

