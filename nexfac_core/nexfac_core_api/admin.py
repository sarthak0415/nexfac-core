from django.contrib import admin
from .models import User, Asset, Area, Task

# Register your models here.
admin.site.register([User, Asset, Area, Task])
