from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Foods)
admin.site.register(User_Fridge)
admin.site.register(Recipes)