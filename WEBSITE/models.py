from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class registertable(models.Model):
    uname=models.IntegerField()
    name=models.CharField(max_length=300)
    #department=models.CharField(max_length=300)
    #year=models.IntegerField(max_length=120)
    email=models.EmailField(max_length=120)
    password=models.CharField(max_length=300)
    reg_type=models.CharField(max_length=300)
    

    
    def __str__(self):
        return u'%s %s %s %s' % (self.name,self.uname,self.email,self.reg_type)