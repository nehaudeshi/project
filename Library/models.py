from django.db import models

# Create your models here.

class Tech_Model(models.Model):
    icon=models.ImageField()
    book_name= models.CharField(max_length=100)
    book_author= models.CharField(max_length=50)
    issued= models.BooleanField()
    copies= models.IntegerField()


    def __str__(self):
        return self.book_name


class Chem_Model(models.Model):
    icon=models.ImageField()
    book_name= models.CharField(max_length=100)
    book_author= models.CharField(max_length=50)
    issued= models.BooleanField()
    copies= models.IntegerField()


    def __str__(self):
        return self.book_name

class Elec_Model(models.Model):
    icon=models.ImageField()
    book_name= models.CharField(max_length=100)
    book_author= models.CharField(max_length=50)
    issued= models.BooleanField()
    copies= models.IntegerField()


    def __str__(self):
        return self.book_name

class Bio_Model(models.Model):
    icon=models.ImageField()
    book_name= models.CharField(max_length=100)
    book_author= models.CharField(max_length=50)
    issued= models.BooleanField()
    copies= models.IntegerField()


    def __str__(self):
        return self.book_name

class Mech_Model(models.Model):
    icon=models.ImageField()
    book_name= models.CharField(max_length=100)
    book_author= models.CharField(max_length=50)
    issued= models.BooleanField()
    copies= models.IntegerField()


    def __str__(self):
        return self.book_name