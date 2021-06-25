from django.contrib import admin

# Register your models here.
from .models import Postac,Rola,Pozycja


admin.site.register(Postac)
admin.site.register(Rola)
admin.site.register(Pozycja)
