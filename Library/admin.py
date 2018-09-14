from django.contrib import admin
from .models import Tech_Model,Chem_Model,Mech_Model,Elec_Model,Bio_Model
# Register your models here.

admin.site.register(Tech_Model)
admin.site.register(Bio_Model)
admin.site.register(Elec_Model)
admin.site.register(Chem_Model)
admin.site.register(Mech_Model)
