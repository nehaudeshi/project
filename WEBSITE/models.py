from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
class userid(models.Model):
    uid = models.CharField(max_length=100)
    session_key = models.CharField(max_length=100)
    def __str__(self):
        return self.uid