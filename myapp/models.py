from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # Añadir el campo description
    file = models.FileField(upload_to='games/', blank=True, null=True)
    unity_play_url = models.URLField(blank=True, null=True)  # Añadir el campo unity_play_url
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title