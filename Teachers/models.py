from django.db import models
#from WEBSITE.models import registertable
class edit(models.Model):
	fname=models.CharField(max_length=300)
	lname=models.CharField(max_length=300)
	sapid=models.IntegerField()
	contact=models.IntegerField()
	email=models.EmailField(max_length=120)
	date=models.DateField()
	prof=models.TextField(max_length=600)
	#qid = models.ForeignKey(Qualification, on_delete=models.CASCADE)
	#sid = models.ForeignKey(specialization)
	about=models.TextField()
	def __str__(self):
		return u'%s %s %s %s %s %s %s' % (self.fname,self.lname,self.sapid,self.contact,self.email,self.date,self.prof,)
class qualification(models.Model):
	qid = models.IntegerField()
	degree = models.CharField(max_length=100)
	year = models.IntegerField()
	institute = models.CharField(max_length=200)
	def __str__(str):
		return u'%s %s %s %s' % (self.qid,self.degree,self.year,self.institute)







# Create your models here.

