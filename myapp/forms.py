
from email.headerregistry import Group
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

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
        role = self.cleaned_data['role']
        if role == 'tester':
            user.groups.add(Group.objects.get(name='Testers'))
        elif role == 'developer':
            user.groups.add(Group.objects.get(name='Developers'))
        if commit:
            user.save()
        return user
