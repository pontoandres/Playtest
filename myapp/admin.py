from django.contrib import admin

from .models import CustomUser, Game, Comment

# Register your models here.
admin.site.register(Game)
admin.site.register(CustomUser)
admin.site.register(Comment)
