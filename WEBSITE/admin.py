from django.contrib import admin
from .models import registertable
#from abstract_base_user_sample import registertable
# Register your models here.
#AUTH_USER_MODEL('registertable')
admin.site.register(registertable)