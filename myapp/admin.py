from django.contrib import admin

from .models import CustomUser, Game

# Register your models here.
admin.site.register(Game)
admin.site.register(CustomUser)