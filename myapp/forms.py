from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import CustomUser, Game

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = (
        ('tester', 'Tester'),
        ('developer', 'Developer'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()  # Guarda el usuario primero para que tenga un ID
            role = self.cleaned_data['role']
            if role == 'tester':
                user.groups.add(Group.objects.get(name='Testers'))
            elif role == 'developer':
                user.groups.add(Group.objects.get(name='Developers'))
        return user

class GameUploadForm(forms.ModelForm):
    unity_play_url = forms.URLField(required=False, help_text="URL del juego en Unity Play")

    class Meta:
        model = Game
        fields = ['title', 'description', 'file', 'unity_play_url', 'image']