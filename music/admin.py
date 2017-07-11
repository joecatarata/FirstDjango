from django.contrib import admin
from .models import Album
#create admin with python manage.py createsuperuser
# Register your models here.

admin.site.register(Album)
